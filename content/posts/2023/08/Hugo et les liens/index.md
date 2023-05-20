---
title: "Hugo et les liens"
date: 2023-08-01
draft: false
tags: ["Liens","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "lien.webp"
toc: true
---
## Liens externes
En markdown c'est facile, mais ça ne gère pas *"ouvrir dans un nouveau onglet"*:
{{< highlight md >}}
[wikipedia](https://fr.wikipedia.org/)
{{< /highlight >}}
[Wikipedia](https://fr.wikipedia.org/)

On pourrait aussi utiliser le shortcode [rawhtml]({{< ref "Hugo-shortcode-Html" >}}).

{{< highlight go-html-template >}}
{{</* rawhtml */>}}
<a href="https://fr.wikipedia.org/" target="_blank">Wikipedia</a>
{{</* /rawhtml */>}}
{{< /highlight >}}
target="_blank" --> nouvelle onglet

{{< rawhtml >}}
<a href="https://fr.wikipedia.org/" target="_blank">Wikipedia</a>
{{< /rawhtml >}}


## Liens internes
Organisation du site:
{{< highlight bash >}}
├── 2023
│   ├── 02
│   │   ├── Diceware
│   │   │   ├── diceware.png-369a6.webp
│   │   │   ├── index.md
│   │   │   └── one-red-dice-01-a9bf3.webp
│   │   ├── Ebook-avec-Latex
│   │   │   ├── epub.wepb
│   │   │   ├── files
│   │   │   │   ├── intro.epub
│   │   │   │   ├── latex2.txt
│   │   │   │   ├── latex_pirates.zip
│   │   │   │   └── latex.txt
│   │   │   ├── index.md
│   │   │   ├── intro.epub
│   │   │   ├── latex2.txt
│   │   │   ├── latex_pirates.zip
│   │   │   ├── latex.txt
│   │   │   └── organisation_livre-cc1fc.webp
│   │   ├── _index.html
{{< /highlight >}}

- Pour rediriger vers un article.
{{< highlight go-html-template >}}
[Latex-les liens]({{</* ref "Latex_Liens" */>}}  "Latex")
{{< /highlight >}}
[Latex-les liens]({{< ref "Latex_Liens" >}}  "Latex")
{{< bandeau success>}}
 Dans la derniere partie du code, *"Latex"* sert au survol du lien.
{{< /bandeau >}}

### Lien vers une autre section
J'ai une section wiki, pour lier un lien, il faut spécifier que c'est dans un autre dossier.

{{< highlight go-html-template >}}
[Mes shortcodes]({{</* ref "/wiki/Mes_Shortcodes.md" */>}}  "Shortcode")
{{< /highlight >}}

[Mes shortcodes]({{< ref "/wiki/Mes_Shortcodes.md" >}}  "Shortcode")

- Page *A propos*.

{{< highlight go-html-template >}}
[A propos]({{</* ref "/pages/apropos.md" */>}}  "A propos")
{{< /highlight >}}
[A propos]({{< ref "/pages/apropos.md" >}}  "A propos")


### Les ancres
Avec Hugo les chapitres deviennent des ancres.

Quand on regarde le code source de la page le 1er chapitre devient:

{{< highlight html >}}
<h2 id="liens-externes">Liens externes</h2>
{{< /highlight >}}

{{< bandeau warning >}}
Attention: Plus de majuscules et les espaces deviennent des *-*.
{{< /bandeau >}}

{{< highlight go-html-template >}}
[liens externe]({{</* ref "#liens-externes" */>}})
{{< /highlight >}}
[Liens externe]({{< ref "#liens-externes" >}})

- Pour lier une ancre d'une autre page.

{{< highlight go-html-template >}}
[Mermaid exemple]({{</* ref "Hugo_shortcode_mermaid.md#exemples" */>}}  "Mermaid exemple")
{{< /highlight >}}

[Mermaid exemple]({{< ref "Hugo_shortcode_mermaid.md#exemples" >}}  "Mermaid exemple")

### Personalisation d'une ancre
On peut personaliser le nom en ajoutant {ancre} a coté du chapitre. 
{{< highlight md >}}
## Instances qui marchent {id="drawio"} 
{{< /highlight >}}

[Drawnio]({{< ref "Drawio_SignauxSncf.md#drawio" >}})

{{< bandeau success>}}
J'ai trouvé plus facile de recuperer les ancres via le code source de la page généré.
{{< /bandeau >}}


## Lien

https://gohugo.io/content-management/cross-references/

{{< chat cactus-comments >}}
