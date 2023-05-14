---
title: "Hugo CMS"
date: 2023-04-06
draft: false
tags: ["Markdown", "HTML","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "hugo.webp"
toc: true
---
{{< figure src="hugo.webp" title="" width=200px class="imagearticle" >}}

[Hugo](https://gohugo.io/) est générateur de site statique. On écrit un article au format  [Markdown](https://fr.wikipedia.org/wiki/Markdown), on fait tourner le logiciel et il fait les fichiers HTML.
Il suffira juste de les déposer sur un serveur.
Ça semble simple  mais ça demande une mise en place.

## Installation
{{< highlight bash >}}
$ sudo apt install hugo
{{< /highlight >}}

## Créer un site
le logiciel va générer un dossier avec les bases (dossiers, fichiers) a l’intérieur.
{{< highlight bash >}}
$ hugo new site schrek.fr
$ cd schrek.fr
{{< /highlight >}}

## Thème
Par défaut, il y a pas de thème, On va en installer un. C’est plus ou moins la même procédure pour tous les [thèmes Hugo](https://themes.gohugo.io/). 
On va utiliser le thème [Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke)
{{< highlight bash>}}
$ git init
$ git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
$ echo "theme = 'ananke'" >> config.toml
{{< /highlight >}}

## 1ᵉʳ article
c’est la méthode pour créer des articles.
{{< highlight bash >}}
$ hugo new posts/info.md
$ nano content/posts/info.md
{{< /highlight >}}

draft indique si l’article est en mode brouillon

{{< highlight markdown>}}
---
title: "Lorem ipsum"
date: 2023-04-06T20:13:42+02:00
draft: true
---
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
{{< /highlight >}}

## 2ᵉ article
On dépose ce fichier dans le dossier /content/posts. C’est le dossier des articles .


[markdown.md](markdown.md.txt)

à renomer markdown.md


## Configuration
Le fichier de configuration (config.toml) se trouve à la racine du site.
Sur le site du thème il y a un exemple de fichier de [configuration](https://github.com/theNewDynamic/gohugo-theme-ananke/blob/master/exampleSite/config.toml)

on dépose un logo dans le dossier static/img . 
{{Attention de bien mettre le bon lien dans BaseURL}}

{{< highlight bash >}}
$ nano config.toml
{{< /highlight >}}

{{< highlight toml>}}
baseURL = 'https://schrek.fr/hugo'
languageCode = 'fr-FR'
title = 'schrek.fr'
theme = 'ananke'
DefaultContentLanguage = "fr"
[params]
  site_logo = "img/logo.svg"
  text_color = ""
  author = "christophe"
  favicon = ""
  description = "The last theme you'll ever need. Maybe."
  # choose a background color from any on this page: https://tachyons.io/docs/themes/skins/ and preface it with "bg-"
  background_color_class = "bg-black"
  recent_posts_number = 3

# Liens sociaux
[[params.ananke_socials]]
name = "twitter"
url = "https://twitter.com/theNewDynamic"

[[params.ananke_socials]]
name = "github"
url = "https://github.com/theNewDynamic"

[[params.ananke_socials]]
name = "mastodon"
url = "https://social.example.com/@username"
rel = "me noopener"

## Traduction 
[languages.fr]
name = "Français"
weight = 2

  [languages.fr.params]
  read_more_copy = "En savoir plus à ce sujet"

[sitemap]
  changefreq = "monthly"
  priority = 0.5
  filename = "sitemap.xml"
{{< /highlight >}}

On lance le serveur 
{{< highlight bash >}}
$ hugo server -D
{{< /highlight >}}

http://localhost:1313/

pour générer le site, on lance.
Il suffira d’envoyer le contenu du dossier public/ sur le serveur. 
{{< highlight bash >}}
$ hugo
{{< /highlight >}}

## Résultat
https://schrek.fr/hugo/



## Liens
https://gohugo.io/

https://bout2code.fr/tutos/creer-un-site-avec-hugo/

https://fr.wikipedia.org/wiki/Hugo_(logiciel)

https://themes.gohugo.io/

https://retrolog.io/blog/creating-a-hugo-theme-from-scratch/

https://transform.tools/yaml-to-toml

https://kinsta.com/fr/blog/hugo-site-statique/

{{< chat cactus-comments >}}
