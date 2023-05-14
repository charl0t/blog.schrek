---
title: "Hugo - Création d’un menu"
date: 2023-05-07
draft: false
tags: ["Markdown", "HTML","Hugo","Menu"]
categories: ["Web"]
series: ["Hugo"]
image: "hugo.webp"
toc: true
---
{{< figure src="hugo.webp" title="" width=200px class="imagearticle" >}}

On va rajouter un menu a notre template. 

## Intro
On pourrait passer par le HTML en ajoutant dans le *header* ou dans un fichier *partial/nav.html* et en l'ajoutant dans le *base_of.html*.

{{< highlight html >}}
<nav> 
 <ul> 
  <li><a href="/">Home</a></li> 
  <li><a href="/about">About</a></li> 
  <li><a href="/contact">Contact</a></li> 
 </ul> 
</nav>
{{< /highlight >}}

Mais Hugo permet de faire plus efficace.
il faut créer dans *themes/MONTHEME/layouts/partials/* un fichier *nav.html*.

{{< highlight html >}}
<nav>
 <ul>
  {{ range .Site.Menus.main }}
   <li><a href="{{ .URL }}">{{ .Name }}</a></li>
  {{ end }}
 </ul>
</nav>
{{< /highlight >}}

## Explication 
On demande a Hugo de regarder dans le fichier de configuration *config.toml*, s'il y a un *Menus.main* et de lister ce qu'il y a en argument.

On ajoute ça a la suite de notre *config.toml* (celui a la racine du site) pour lui indiquer notre menu.

{{< highlight toml >}}
[menu]
[[menu.main]]
  name = 'Home'
  url = '/'
  weight = 10
[[menu.main]]
  name = 'About'
  url = 'pages/about/'
  weight = 20
{{< /highlight >}}

Pour insérer le menu dans le template on va le rajouter a header.html dans le dossier */themes/MONTHEME/layouts/partials*.

{{< highlight html >}}
<header>
<h1 class="titre">{{ .Site.Title }}</h1>
<h2 class="soustitre">{{ .Site.Params.description }}</h2>
        {{- partial "nav.html" . -}}
</header>
{{< /highlight >}}

{{< figure src="screenshot.webp" title="" width=600px class="imagearticle" >}}

## CSS
un coup de CSS pour aligner tous ça  dans le dossier *schrek.fr/themes/hugo-latex/static/css/style.css*.

{{< highlight css >}}
nav ul li {
       display: inline;
	list-style: none;

}
nav li::before {
     content: ""; 
     padding-right: 2rem;
}
{{< /highlight >}}


## Résultat
On se replace à la racine du projet pour lancer, les options permettent de voir les modifications en direct.

{{< highlight bash >}}
$ hugo serve --noHTTPCache --ignoreCache --disableFastRender
{{< /highlight >}}

https://schrek.fr/hugo1/

## Lien
https://bout2code.fr/tutos/creer-un-site-avec-hugo/

{{< chat cactus-comments >}}


