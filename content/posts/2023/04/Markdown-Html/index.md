---
title: "Markdown to Html"
date: 2023-04-14
draft: false
tags: ["Pandoc", "Html"]
categories: ["Web"]
image: "markdown-syntax-language.png"
toc: true
---
{{< figure src="markdown-syntax-language.png" title="" width=200px class="imagearticle" >}}

Pandoc est une application en ligne de commande qui permet de convertir des documents dans différents format. 

On va l’utiliser pour créer un page HTML a partir d’un document créer avec les balises Markdown, pour plus de "beauté on va y inclure un fichier Css

## Installation Pandoc 
{{< highlight bash >}}
$ sudo apt install pandoc
{{< /highlight >}}

## Utilisation 

On récupère un fichier css (https://latex.vercel.app/ pour l’exemple).
{{< highlight bash >}}
$ wget https://latex.now.sh/style.css
{{< /highlight >}}
J’ai tout ajouté dans le fichier en dessous.

[pando_md_html.zip *(clic droit enregistrer sous)*](pando_md_html.zip)

## Commandes
{{< highlight bash >}}
pandoc --css=style.css -s -f markdown --toc --metadata \pagetitle="Titre" --to=html5 test.md -o index.html
{{< /highlight >}}
La commande est facile a comprendre
 s “standalone” s’occupe du header
 toc table des matieres

## Liens
https://pandoc.org/

https://latex.vercel.app/



