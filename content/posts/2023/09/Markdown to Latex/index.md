---
title: "Convertir de Markdown vers Pdf"
date: 2023-09-10
draft: false
tags: ["Latex","Markdown","Pandoc","Pdf"]
categories: ["Latex"]
series: ["Latex"]
image: "logo.webp"
toc: true
---
[Pandoc](https://pandoc.org/) est un super outils de convertion, On va convertir un fichier Markdown en Pdf, en passant par Latex.

*Vous avez les fichiers en bas de la page.*

## L'entête du fichier Markdown
On va configurer le début du fichier Markdown avec l'aide de la documentation [Pandoc.](https://pandoc.org/MANUAL.html#variables-for-latex)

{{< highlight toml >}}
---
title: Mon super titre
subtitle: Sous titre
date: \today 
documentclass: scrartcl
papersize: a4
lang: fr-FR
geometry:
- left=2cm
- right=2cm
- top=2cm
- bottom=2cm
colorlinks: true
linkcolor: blue
urlcolor: blue
fontsize: 12pt
toccolor: ProcessBlue
---
{{< /highlight >}}

## La commande sous Linux
Ensuite on lance la commande:

{{< highlight bash >}}
$ pandoc --from=markdown   --toc  --output=test.pdf test.md
{{< /highlight >}}

- *--toc* :Table des matières


## Fichiers
{{< pj />}}

## Liens
https://pandoc.org/MANUAL.html#variables-for-latex

https://programminghistorian.org/fr/lecons/redaction-durable-avec-pandoc-et-markdown

{{< chat cactus-comments >}}
