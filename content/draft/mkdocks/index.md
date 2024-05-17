---
title: "Mkdocs pour le documentation"
date: 2024-01-15
draft: true
tags: ["Mkdocs", "Python","Documentation","Markdown"]
categories: ["Web"]
Image: "mkdocs.webp"
toc: true
---

On a tous eu besoin a un moment d’écrire de la documentation, [Mkdocs](https://www.mkdocs.org/) est une solution facile à mettre en place.
Écrit en python, il utilise le langage [Markdown](https://docs.framasoft.org/fr/grav/markdown.html) pour écrire votre documentation

<!--more-->

## Installation
Facile avec le gestionnaire de paquet [pip](https://fr.wikipedia.org/wiki/Pip_(gestionnaire_de_paquets)).

{{< highlight bash  >}}
$ pip install mkdocs
{{< /highlight >}}

On va créer notre projet 


{{< highlight bash  >}}
$ mkdocs new test
$ cd test
$ ls
docs  mkdocs.yml
{{< /highlight >}}

On lance le serveur 

{{< highlight bash  >}}
$ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.09 seconds
INFO    -  [18:29:11] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [18:29:11] Serving on http://127.0.0.1:8000/
INFO    -  [18:29:14] Browser connected: http://127.0.0.1:8000/
{{< /highlight >}}

Voila, c'est fini. On se connecte sur le lien et on a une version brut de Mkdocs


## Ecrire


{{< highlight bash  >}}
site_name: MkLorum
site_url: https://example.com/
nav:
  - Home: index.md
  - About: about.md
  - Markdown: Markdown/markdown.md
theme:
  name: mkdocs
  locale: fr
{{< /highlight >}}


## changer de theme
https://squidfunk.github.io/mkdocs-material/

{{< highlight bash  >}}
$ pip install mkdocs-material
{{< /highlight >}}


## Construire le site
{{< highlight bash  >}}
$ mkdocs build
{{< /highlight >}}
Les fichiers HTML se trouve dans le dossier *site*, faut simplement les transférer sur le serveur.

## Liens




