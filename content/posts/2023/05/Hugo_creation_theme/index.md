---
title: "Hugo - Création d’un thème"
date: 2023-05-05
draft: false
tags: ["Markdown", "Html","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "hugo.webp"
toc: true
---
{{< figure src="hugo.webp" title="" width=600px class="imagearticle" >}}

Après l’article sur l'installation d'Hugo et la mise en place d’un thème, on va créer notre thème perso.

On se place dans le dossier de notre projet.

{{< highlight bash >}}
$ hugo new theme christophe
$ cd themes/christophe/
$ tree
.
├── archetypes
│   └── default.md (modeles pour les articles et les pages)
├── layouts
│   ├── 404.html
│   ├── _default
│   │   ├── baseof.html (page qui structure les autres pages)
│   │   ├── list.html ( exemple la liste des articles)
│   │   └── single.html (un article )
│   ├── index.html (page d'accueil)
│   └── partials
│       ├── footer.html (pied de page)
│       ├── header.html (haut de page)
│       └── head.html (entete html)
├── LICENSE
├── static  ( dossier ou l'on met les images/css/java) 
│   ├── css
│   └── js
└── theme.toml
{{< /highlight >}}

Hugo a créé une organisation minimale pour un projet.

## Petites explications

Hugo appel la page *baseof.html* et la complète avec une autre page.

{{< highlight html >}}
<!DOCTYPE html>
<html>
    {{- partial "head.html" . -}}
    <body>
        {{- partial "header.html" . -}}
        <div id="content">
        {{- block "main" . }}{{- end }}
        </div>
        {{- partial "footer.html" . -}}
        {{- partial "script.html" . -}}
    </body>
</html>
{{< /highlight >}}

Si je prends la page d’accueil, il va rajouter le contenu d’index.html a  {{- block "main" . }}{{- end }}

Pour les articles il va ajouter single.html 

## Head
*themes/hugo-latex/layouts/partials/head.html*

On va utiliser comme base le [CSS latex](https://latex.vercel.app/) 

{{< highlight html >}}
<head>
    <html lang="fr">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ .Site.Title }}</title>
    <link rel="stylesheet" href="https://latex.now.sh/style.css"> 
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="stylesheet" href="https://latex.now.sh/prism/prism.css">
    <script src="https://cdn.jsdelivr.net/npm/prismjs/prism.min.js"></script> 
    <link href="{{ .Site.BaseURL }}css/style.css" rel="stylesheet">
</head>
{{< /highlight >}}

 {{ .Site.Title }} est remplacé par Hugo par le nom du site indiqué dans le fichier de configuration config.toml “title = 'schrek.fr'”
 
 <link href="{{ .Site.BaseURL }}css/style.css" rel="stylesheet"> : indique l'emplacement du CSS perso (themes/hugo-latex/static/css)

## Header
*themes/hugo-latex/layouts/partials/header.html*

{{< highlight html >}}
<header>
<h1 class="titre">{{ .Site.Title }}</h1>
<h2 class="soustitre">{{ .Site.Params.description }}</h2>
</header>
{{< /highlight >}}

{{ .Site.Params.description }} est remplacé par Hugo par le nom du site indiqué dans le fichier de configuration *config.toml*.

## Footer
*themes/hugo-latex/layouts/partials/footer.html*

{{< highlight html >}}
<footer>
    © 2023 {{ .Site.Title }}
<button id="dark-mode-toggle">Toggle dark mode</button>
</footer>
{{< /highlight >}}



{{< highlight toml >}}
[params]
description = 'Mon super site sous hugo'
{{< /highlight >}}

## Lists
*themes/hugo-latex/layouts/_default/list.html*

Pour l'affichage des listes. 

{{< highlight html >}}
{{ define "main" }}
<main>
<div class="container">
<div class="content">
    <ul>
    <!-- Ranges through content/post/*.md -->
    {{ range .Pages }}
        <li>
            <h2><a href="{{.Permalink}}">{{.Title}}</a></h2>
           <div class="content"> 
           <i>{{.Date.Format "2006-01-02"}}</i></br>
            {{ .Summary }}
            {{ if .Truncated }}
            <div class="read-more-link">
            <a href="{{ .RelPermalink }}">Lire plus...</a>
            </div>
            {{ end }}
            </div>
        </li>
    {{ end }}
    </ul>
</div>
</div>
</main>
{{ end }}
{{< /highlight >}}

## Single
*themes/hugo-latex/layouts/_default/single.html*

Pour l'affichage des articles. 

{{< highlight html >}}
{{ define "main" }}
<div class="cartouche">
 <h1>{{ .Title }}</h1>
<i>{{ .PublishDate.Format "2006-01-02" }}</i>
        <ul>
    {{ range (.GetTerms "tags") }}
        <li><span class="tag">
            <a href="{{ .Permalink }}">{{ .LinkTitle }}</a></li>
        </li>
        </spam>    
    {{ end }}
        </ul>
</div>
<article>
{{ .Content }}
</article>
{{ end }}
{{< /highlight >}}

## Index
*themes/hugo-latex/layouts/index.html*

Page d'accueil 

{{< highlight html >}}
{{ define "main" -}}
{{ .Content }}
<div class="container">
<div class="content">
{{- range where .Site.RegularPages "Section" "posts" -}}
<article>
<h3 class="post-title">
<a href="{{ .Permalink }}">{{ .Title }}</a>
</h3>
<time datetime="{{ .Date.Format "2006-01-02T15:04:05Z0700" }}" class="post-date">{{ .Date.Format "Mon, Jan 2, 2006" }}</time>
{{ .Summary }}
{{ if .Truncated }}
<div class="read-more-link">
<a href="{{ .RelPermalink }}">Lire plus...</a>
</div>
{{ end }}
</article>
{{- end }}
</div>
</div>
{{- end }}
{{< /highlight >}}

## CSS perso
*/themes/hugo-latex/static/css/style.css*


{{< highlight css >}}
body {
	display: flex;
	flex-direction: column;
	max-width: 140ch;
}
main {
	flex: 1;	
}
header {
border-bottom: 1px solid;
}
.titre {
text-align: center;
}
.soustitre {
text-align: center;
font-style: italic;
}
.cartouche ul li {
    display: inline;
	list-style: none;
	margin-left: 1rem;
	margin-top: 0em;
    padding: 0.3rem;
    border: 1px solid;
    border-radius: 10px 40px 40px 10px;
    background: #e6e5e5;
}
footer {
position:  initial;
border-top: 1px solid;
bottom: 0;
text-align: center;
margin-top: 2rem;
}
article {
text-align: left;
}
h1:first-child {
text-align: left;
}
{{< /highlight >}}


## Résultat
On se replace à la racine du projet pour lancer, les options permettent de voir les modifications en direct.

{{< highlight bash >}}
$ hugo serve --noHTTPCache --ignoreCache --disableFastRender
{{< /highlight >}}

Cela devrait donner https://schrek.fr/hugo1/


## Liens
https://jamstatic.fr/2018/03/10/mettre-en-place-son-premier-site-sous-hugo/#3-personnaliser-votre-site

https://www.goglides.dev/bkpandey/create-a-hugo-theme-from-scratch-20a8

https://bout2code.fr/tutos/creer-un-site-avec-hugo/

{{< chat cactus-comments >}}
