---
title: "Notes dans Latex"
date: 2024-12-01
draft: false
tags: ["Latex","Notes"]
categories: ["Latex"]
Image: "latex_logo.webp"
toc: true
---

Le package todonotes est un outil puissant pour gérer des annotations et des commentaires dans un document LaTeX. Très pratique pour collaborer ou pour organiser le processus de rédaction, il permet d’insérer des notes visuelles dans la marge ou directement dans le texte.

<!--more-->

## Installation et préambule

Pour utiliser todonotes, ajoutez simplement cette ligne dans le préambule de votre document LaTeX :

{{< highlight tex >}}
\usepackage{todonotes}
{{< /highlight >}}

## Fonctions principales

### Ajouter une note dans la marge:

{{< highlight tex >}}
\todo{Texte de la note}
{{< /highlight >}}

### Insertion d’une note dans le texte:
{{< highlight tex >}}
\todo[inline]{Texte de la note}
{{< /highlight >}}

### Personaliser des notes

Vous pouvez personnaliser la couleur ou l’apparence des annotations.

{{< highlight tex >}}
\todo[color=red!50]{Note urgente.}
{{< /highlight >}}

### Désactivation des notes

Pour produire une version finale sans notes, désactivez simplement les commandes du package avec :

{{< highlight tex >}}
\usepackage[disable]{todonotes}
{{< /highlight >}}

## Fichiers
D'autres exemple dans les fichiers.

{{< pj />}}

## Liens

https://tug.ctan.org/macros/latex/contrib/todonotes/todonotes.pdf

https://fr.overleaf.com/latex/examples/example-formatted-todonotes/qmpbkcqxfgmg

https://latex-tutorial.com/boost-latex-productivity-todo-notes/
