---
title: "Re-organisation du site"
date: 2023-05-08
tags: ["Hugo"]
categories: ["Web"]
image: "hugo.webp"
series: ["Hugo"]
toc: true
draft: false
---
Je commençais à me mêler les pinceaux avec tous les articles, j'ai décider de changer l'organisation du site.

Je voulais aussi des URL *lisibles*

{{< figure src="site-hierarchy.webp" title="" width=600px class="imagearticle" >}}

## Nouvelle organisation
J'ai organisé mon dossier *content* comme sur le diagramme dessous, les articles seront rangés par date (année, mois). 

{{< mermaid >}}
 flowchart LR
    A[Schrek.fr]-->B(Pages)
    B-->F[About]
    B-->G[search]
    A-->C[Posts]
    D-->K[Pages]
    C-->E[2023]
    E-->H(01)
    E-->I(02)
    E-->J(03) 
    A-->D[Wiki]
{{< /mermaid >}}

# Les URLs
Dans mon ficher *config.toml*, j'ai rajouté:

{{< highlight toml >}}
[permalinks]
  '/' = '/:year/:month/:title/'
{{< /highlight >}}
[*Source Hugo*](https://gohugo.io/content-management/urls/#permalinks-examples)


## Liens
https://gohugo.io/content-management/urls/


{{< chat cactus-comments >}}
