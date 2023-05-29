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

{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/pcvxfjxmmqvh" icone="forward" >}}

## Lien dans un document
{{< highlight tex >}}
\hyperlink{ID}{TEXT}
{{< /highlight >}}

{{< highlight tex >}}
\hypertarget{ID}{TEXT}
{{< /highlight >}}


## Liens
https://ctan.org/pkg/hyperref

https://www.overleaf.com/learn/latex/Hyperlinks

https://www.xm1math.net/doculatex/url.html






{{< chat cactus-comments >}}
