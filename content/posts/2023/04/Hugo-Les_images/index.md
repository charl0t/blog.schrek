---
title: "Hugo et les images"
date: 2023-04-01
draft: false
tags: ["Markdown", "Html","Hugo","Shortcode"]
categories: ["Web"]
series: ["Hugo"]
image: "hugo.webp"
toc: true
---
## Comment ca marche?
L’organisation des images avec Hugo, c’est un peu particulier.

Avec Markdown on ajoute une image avec:

{{< highlight markdown >}}
![Text alternatif](image.jpg)
{{< /highlight >}}


## Dossier static
C'est le dossier ou l'on pose nos fichiers statique .

On peut organiser comme ça: 

je fais un post info et je place les images dans un sous dossier static/posts/info

{{< highlight Bash >}}
static/
├── css
├── img
│   └── posts
│       └── info
│           └── image.jpg
└── js

{{< /highlight >}}


Ce qui donne dans un post:

{{< highlight markdown >}}
![Text alternatif](/img/posts/info/hugo.jpg)
{{< /highlight >}}

## Dossier content
La solution la plus facile a mon goût.
On va créer pour chaque article un dossier, et chaque article sera dans un dossier index.html ou va se retrouver le contenue de l'article.
cela va permettre de mettre les images dans le dossier de l’article et ça évite de se disperser.

{{< highlight Bash >}}
content/
└── posts
    ├── lettre
    │   ├── hugo.jpg
    │   ├── index.md
    │   └── lettre.pdf
    ├── info
    │   ├── images.png
    │   └── index.md
    └── markdown
        └── index.md
 
{{< /highlight >}}
Ce qui donne dans un post:
{{< highlight markdown >}}
![Text alternatif](hugo.jpg)
{{< /highlight >}}

## Shortcode interne
On peut utiliser aussi le shortcode interne au moteur d’Hugo
{{< highlight bash >}}
{{< figure src="Capture.png" title="" width=600px class="imagearticle" >}}
{{< /highlight >}}


{{< chat cactus-comments >}}

