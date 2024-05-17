---
title: "QRcode sous LaTex"
date: 2023-02-20
draft: false
tags: ["Qrcode"]
categories: ["Latex"]
image: "qrcode_wikipedia.webp"
toc: true
---
{{< figure src="qrcode_wikipedia.webp" title="" width=200px class="imagearticle" >}}

On peut produire facilement des [QRCode](https://fr.wikipedia.org/wiki/Code_QR) sous LaTex.

## Installation
On récupère les fichiers  qrcode.ins et qrcode.dtx [ici](https://www.ctan.org/tex-archive/macros/latex/contrib/qrcode).
On lance sous Linux:

{{< highlight bash >}}
$ latex qrcode.ins
{{< / highlight >}}

Il faut ajouter dans l’entête du fichier latex 


{{< highlight tex >}}
\usepackage{hyperref} % Pour avoir les liens
\usepackage{qrcode} % Pour générer les QRcode
{{< / highlight >}}


## Utilisation

{{< highlight tex >}}
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
\usepackage[T1]{fontenc}
\usepackage{fullpage}
\usepackage{hyperref}
\usepackage{qrcode}
\usepackage{graphicx} % Pour inclure des images

%titre
\title{QRcode avec \LaTeX}

\date{}
\begin{document}
\maketitle
\subsection*{QRcode simple}
\begin{verbatim}
\qrcode{http://schrek.fr}
\end{verbatim}
\begin{center}
\qrcode{http://schrek.fr}
\end{center}
\subsection*{QRcode simple avec la version 3 qui permet plus de caractères.}
\includegraphics[width=7cm]{QR-Code-versions.jpg}
\begin{verbatim}
\qrcode[nolink,version=3]{j'aime pas la soupe}
\end{verbatim}
\begin{center}
\qrcode[nolink,version=3]{j'aime pas la soupe}
\end{center}
\subsection*{QRcode avec lien et taille(1,5cm.}
\begin{verbatim}
\qrcode[link, version=3, height=1.5cm]{http://schrek.fr}
\end{verbatim}
\begin{center}
\qrcode[hyperlink,height=2cm]{http://schrek.fr}
\end{center}
\end{document}
{{< / highlight >}}


## Résultat PDF

[Téléchargement](exemple2.pdf)

## Lien

https://blog.dorian-depriester.fr/latex/generer-des-qr-codes-directement-dans-latex


