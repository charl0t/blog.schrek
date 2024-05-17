---
title: "Latex et les liens"
date: 2023-08-20
draft: false
tags: ["Latex","hyperref"]
categories: ["Latex"]
series: ["Latex"]
image: "lien.webp"
toc: true
---
Le module [*hyperref*](https://ctan.org/pkg/hyperref) permet de créer des liens externes et interne sur un PDF.

On peut changer les couleurs et ajouter des métadonnées

Son utilisation est facile.

## Utilisation

Pour un lien simple:
{{< highlight tex >}}
\url{https://wikipedia.fr}
{{< /highlight >}}

Pour un un liens dans le texte:
{{< highlight tex >}}
\href{https://wikipedia.fr}{Wikipedia.fr} 
{{< /highlight >}}

Pour un email:
{{< highlight tex >}}
\href{mailto:madame@michu.fr}{madame@michu.fr}
{{< /highlight >}}

Pour un document (Attention au chemin):
{{< highlight tex >}}
\href{run:./xcolor.pdf}{Voir ce PDF}
{{< /highlight >}}

## Les exemples

{{< highlight tex >}}
\documentclass[a4paper,10pt]{scrartcl} % koma-script
\usepackage{graphicx} % Module images
\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{parskip}
\usepackage[french]{babel} % En francais
\usepackage{hyperref} % Module hyperref
\hypersetup{colorlinks=true,
linkcolor=blue, % Couleurs des liens 
filecolor=magenta, % Couleur des liens de fichier 
urlcolor=cyan,% Couleur des Urls
pdftitle={Hyperref},% Meta titre
pdfauthor={Christophe},% Meta auteur
pdfsubject={Les liens avec Latex},% Meta sujet
pdfkeywords={Latex,Hyperref},% Meta mots clefs 
pdfproducer = Latex}% Meta generateur du pdf

\urlstyle{same} % Meme police pour les urls

\title{Hyperref}
\author{Christophe }
\date{Juin 2023}
\begin{document}

\maketitle

\section*{Liens simples}
\href{https://wikipedia.fr}{Wikipedia.fr} 
\par
\url{https://wikipedia.fr}
\par
\href{mailto:madame@michu.fr}{madame@michu.fr}
\par
\href{run:./xcolor.pdf}{Voir ce PDF}
\end{document}
{{< /highlight >}}

## Lien dans un document
- Pour créer le lien:
{{< highlight tex >}}
\hyperlink{ID}{TEXT}
{{< /highlight >}}

- La cible du lien:
{{< highlight tex >}}
\hypertarget{ID}{TEXT}
{{< /highlight >}}

## Les couleurs
Par defaut, c'est pas trés jolie, mais on peut changer ca:
{{< highlight tex >}}
\hypersetup{colorlinks=true,
linkcolor=blue, % Couleurs des liens 
filecolor=magenta, % Couleur des liens de fichier 
urlcolor=cyan,% Couleur des Urls}
{{< /highlight >}}

## Table des matières
Quand on ajoute une table des matières (à placer après *\begin{document}*), *hyperref* génére des liens pour accéder directement aux chapitres.
{{< highlight tex >}}
\tableofcontents
{{< /highlight >}}

## Métadonnées
On peut aussi ajouter des métadonnées aux documents PDF

{{< highlight tex >}}
\hypersetup{
pdftitle={Hyperref},% Meta titre
pdfauthor={Christophe},% Meta auteur
pdfsubject={Les liens avec Latex},% Meta sujet
pdfkeywords={Latex,Hyperref},% Meta mots clefs 
pdfproducer = Latex}% Meta generateur du pdf}
{{< /highlight >}}

Ce qui donne sous Linux

{{< highlight bash >}}
$ pdfinfo hyperref.pdf 
Title:           Hyperref
Subject:         Les liens avec Latex
Keywords:        Latex,Hyperref
Author:          Christophe
Creator:         LaTeX with hyperref
Producer:        Latex
CreationDate:    Wed May 31 10:55:33 2023 CEST
{{< /highlight >}}

## Exemple presque complet

{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/pcvxfjxmmqvh" icone="forward" >}}

## Liens
https://ctan.org/pkg/hyperref

https://www.overleaf.com/learn/latex/Hyperlinks

https://www.xm1math.net/doculatex/url.html



