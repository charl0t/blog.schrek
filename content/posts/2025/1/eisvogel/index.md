---
title: "Template Eisvogel"
date: 2025-01-10
draft: false
tags: ["Latex","Eisvogel"]
categories: ["Latex"]
Image: "latex_logo.webp"
toc: true
---

Le template Eisvogel est un modèle populaire pour créer des documents PDF de haute qualité avec Pandoc, un convertisseur universel de documents. Ce modèle est spécialement conçu pour produire des documents au format LaTeX qui se distinguent par leur esthétique professionnelle et leur mise en page élégante.

<!--more-->


## Caractéristiques principales d’Eisvogel

Eisvogel est apprécié pour plusieurs raisons, notamment :
- Design moderne et professionnel : Il propose une mise en page soignée, idéale pour des rapports, des articles académiques ou des documents professionnels.
- Compatibilité Markdown : En combinant Pandoc avec Eisvogel, vous pouvez écrire vos documents en Markdown et obtenir des PDF impeccables.
- Personnalisation : Eisvogel permet de personnaliser divers aspects comme les polices, les couleurs, les marges, etc.
- Support des en-têtes et pieds de page : Il gère facilement les en-têtes (headers) et pieds de page (footers) avec numérotation, noms d’auteur, et titres.

## Installation du template Eisvogel

Pour utiliser le template Eisvogel avec Pandoc, voici les étapes à suivre :

### Téléchargez le modèle
Rendez-vous sur le dépôt GitHub d’Eisvogel et téléchargez le fichier eisvogel.tex.

https://github.com/Wandmalfarbe/pandoc-latex-template



### Utilisation du template Eisvogel

Une fois installé, Eisvogel peut être utilisé pour convertir un fichier Markdown en PDF. Voici un exemple de commande de base :

``
pandoc input.md -o output.pdf --from markdown --template eisvogel.tex --pdf-engine=lualatex
``

Options courantes :

- --pdf-engine=lualatex ou --pdf-engine=xelatex : Spécifie le moteur LaTeX utilisé pour la conversion.
- --metadata : Permet d’ajouter des métadonnées comme le titre, l’auteur, ou la date.

Par exemple :

`` pandoc input.md -o output.pdf --template eisvogel --pdf-engine=lualatex --metadata title="Mon Rapport" --metadata author="Jean Dupont" —metadata date="16 novembre 2024" ``

Ajouts personnalisés avec Eisvogel

Eisvogel offre des options supplémentaires pour enrichir vos documents :
- Ouvrir pages de titre : Vous pouvez configurer une page de garde élégante.
- Sections numérotées : Activez la numérotation automatique des sections avec l’option --number-sections.
- Table des matières : Générez une table des matières avec --table-of-contents ou -V toc.

Exemple :

``
$ pandoc test.md -o output.pdf --template eisvogel.tex --table-of-contents
``

Le template est trés bien documenté [ici](https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master/examples), avec pleins d'exemples.



## Liens

https://github.com/Wandmalfarbe/pandoc-latex-template

https://github.com/egeerardyn/awesome-LaTeX

https://github.com/martinbjeldbak/ultimate-beamer-theme-list

