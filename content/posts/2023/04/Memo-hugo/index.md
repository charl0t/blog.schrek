---
title: "Astuces Hugo"
date: 2023-04-06
draft: false
tags: ["Markdown", "HTML","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "hugo.webp"
toc: true
---
{{< figure src="hugo.webp" title="" width=200px class="imagearticle" >}}

## Organisation
{{< highlight bash >}}
├── pages
│   └── apropos
│       ├── hugo-logo.png
│       └── index.md
└── posts
    ├── css_framework
    │   └── index.md
    ├── info
    │   ├── Capture.png
    │   ├── hugo.jpg
    │   └── index.md
    └── markdown
        ├── index.md
        └── logo.png

{{< /highlight >}}


## Debut article 
Avec balise figure

## Images
On ajoute la balise Hugo 

{{< figure src="Capture.webp" title="" width=600px class="imagearticle" >}}

## Menu config.toml

Dans le fichier config.toml et dans le fichier themes/wikischrek/layouts/partials/nav.html

Les icones ici https://getuikit.com/docs/icon
{{< highlight toml >}}
[menu]
[[menu.main]]
  name = 'Home'
  url = '/'
  pre = 'home'
  weight = 10
[[menu.main]]
  name = 'About'
  url = '/pages/apropos/'
  pre = 'info'
  weight = 20
{{< /highlight >}}

## Les commentaires dans le code
pas de commentaire <!-- --> dans la 1er ligne de code des squelettes

## Summary
- Dans un article pour couper le texte sur la page d'acceuil
{{< highlight html >}}
Sans les \
\<!--more--\>
{{< /highlight >}}

- Pour limiter le nombre de mot (par defaut 50), ans le fichier config.toml 

summaryLength = 40


{{< chat cactus-comments >}}

 
