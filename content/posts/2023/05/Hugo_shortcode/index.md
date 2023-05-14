---
title: "Hugo shortcode"
date: 2023-05-10
draft: false
tags: ["Shortcode", "HTML","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "hugo.webp"
toc: true
---
{{< figure src="hugo.webp" title="" width=200px class="imagearticle" >}}

La syntaxe Markdown a des limites, Hugo utilise des « bouts de code » pour passer ces limites. 

L’inconvénient c’est de retenir les balises.

L'avantage est d'intégrer des fonctions au sein même du contenu, sans toucher au template.

## Shortcode interne

Vous trouverez pleins d'exemple sur le site officiel.

https://gohugo.io/content-management/shortcodes/


## shortcodes personnalisés 

### Des icônes
On va se servir des icônes du framework du site.
https://getuikit.com/docs/icon
Pour afficher une icône en HTML c est:
{{< highlight html >}}
<span uk-icon="icon: check"></span>
{{< /highlight >}}

On va créer un dossier *layouts//shortcodes* dans notre thème et un fichier *uicon.html*
Qui va contenir simplement:

{{< highlight html >}}
<span uk-icon="{{- .Get 0 -}}"></span>
{{< /highlight >}}

{{- .Get 0 -}} appel le 1er argument du shortcode 

{{< highlight html >}}
{{</* uicon "heart" */>}} est un cœur.
{{< /highlight >}}

Ceci {{< uicon "heart" >}} est un cœur.

On va rajouter la taille des icônes comme dans la doc de Uikit:

{{< highlight go-html-template >}}
{{ $icon := (.Get 0) }}
{{ $taille := default "1" (.Get 1)}}
<span uk-icon="icon: {{ $icon }}  ; ratio: {{ $taille }}"></span>
{{< /highlight >}}

- {{ $icon := (.Get 0) }} enregistre le parametre dans la variable $icon
- {{ $taille := default "1" (.Get 1)}} enregistre le 2eme paramètre dans la variable $taille et si rien met 1

{{< highlight go-html-template >}}
{{</* uicon heart 2 */>}} est un **gros** coeur.
{{< /highlight >}}

{{< uicon heart 2 >}} est un **gros** coeur.



### Des bandeaux

On va reprendre le CSS de [Uikit](https://getuikit.com/docs/alert) pour faire une barre d’avertissement.
L'idée c'est d'inclure du texte entre 2 balises 

{{< highlight html >}}
<div class="uk-alert-danger" uk-alert>
    <a class="uk-alert-close" uk-close></a>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
</div>
{{< /highlight >}}

{{< highlight go-html-template >}}
<div class="uk-alert-{{- .Get 0 -}}" uk-alert>
    <a class="uk-alert-close" uk-close></a>
    <p>{{ .Inner | markdownify }}</p>
</div>
{{< /highlight >}}

- {{- .Get 0 -}} récupère la 1er variable. 
- {{ .Inner | markdownify }} récupère le texte entre les balises et on garde la syntaxe Markdown.

Les 4 classes de notre CSS:
- primary 	Give the message a prominent styling. (bleu)
- success 	Indicates success or a positive message. (vert)
- warning 	Indicates a message containing a warning. (orange)
- danger 	Indicates an important or error message. (rouge)

On va aussi commenter le code avec les balises HTML 
{{< highlight html >}}
<!-- commentaires -->
{{< /highlight >}}

{{< highlight go-html-template >}}
<!--
https://getuikit.com/docs/alert)
- primary 	Give the message a prominent styling. (bleu)
- success 	Indicates success or a positive message. (vert)
- warning 	Indicates a message containing a warning. (orange)
- danger 	Indicates an important or error message. (rouge)

Utilisation : 
bandeau primary 
-->

<div class="uk-alert-{{- .Get 0 -}}" uk-alert>
    <a class="uk-alert-close" uk-close></a>
    <p>{{ .Inner | markdownify }}</p>
</div>
{{< /highlight >}}

On va créer un fichier *bandeau.html* dans  un dossier *layouts//shortcodes* de notre thème.

On appel notre shortcode dans notre article markdown.

{{< highlight go-html-template >}}
{{</* bandeau primary */>}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{</* / bandeau */>}} 
{{< /highlight >}}

{{< bandeau primary >}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{< / bandeau >}} 

{{< bandeau success >}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{< / bandeau >}} 

{{< bandeau warning >}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{< / bandeau >}} 

{{< bandeau danger >}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{< / bandeau >}} 

Le CSS Pour avoir la bande à gauche.

{{< highlight css >}}
.uk-alert-danger {
border-left: solid;
}
.uk-alert-warning {
border-left: solid;
}

.uk-alert-primary {
border-left: solid;
}
.uk-alert-success {
border-left: solid;
}
{{< /highlight >}}

## Astuce 

{{< bandeau success >}}
### Astuce
Pour voir un article futur et en mode brouillon, on lance Hugo avec cette commande:
 
*$ hugo serve -D -F*

{{< / bandeau >}}

## Liens

https://bout2code.fr/tutos/creer-un-site-avec-hugo/comment-creer-un-site-avec-hugo-partie-8-creer-des-shortcodes/

https://jldblog.eu/post/hugo/hugo_shortcode_lichess_puzzle/

https://jldblog.eu/post/hugo/hugo_shortcode_font_awesome/

https://jamstatic.fr/2017/10/01/templates-hugo-designers-wordpress/

{{< chat cactus-comments >}}
