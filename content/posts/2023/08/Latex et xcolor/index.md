---
title: "Latex et xcolor"
date: 2023-08-15
draft: false
tags: ["Latex","Xcolor"]
categories: ["Latex"]
series: ["Latex"]
image: "xcolor.webp"
toc: true
---
Le paquetage *xcolor* fait partie des indispensables de Latex pour coloriser les textes.

## Préambule
On appelle les couleurs de base de *xcolor*, 

{{< figure src="xcolor1.webp" title="" width=500px class="imagearticle" >}}

{{< highlight tex >}}
\usepackage{xcolor} % import des couleurs dans les textes
{{< /highlight >}}

Il y a aussi d'autres palettes de couleurs:

- dvipsnames: 68 couleurs (CMYK);
- svgnames: 151 couleurs (RGB);
- x11names: 317 couleurs (RGB).
 
{{< highlight tex >}}
\usepackage[dvipsnames]{xcolor} % import des couleurs dans les textes
{{< /highlight >}}

Tous est bien indiqué dans la [documentation (page 39)](https://www.ctan.org/pkg/xcolor).

## Personnalisation des couleurs
On peut aussi créer notre propre palette de couleurs, il suffit de les décrire dans le préambule.

Une palette pour aider à choisir sur [W3schools.com](https://www.w3schools.com/colors/colors_picker.asp).
 
{{< highlight tex >}}
% Les couleurs
\definecolor{violet}{RGB}{110,30,120}
\definecolor{prune}{RGB}{161,0,107}
\definecolor{framboise}{RGB}{205,0,55}
\definecolor{orange}{RGB}{224,82,6}
\definecolor{jaune_safran}{RGB}{255,182,18}
{{< /highlight >}}

## Exemples
{{< highlight tex >}}
\documentclass[a4paper,10pt]{scrartcl} % Koma-script
\usepackage[T1]{fontenc}
\usepackage[french]{babel} % En francais
\usepackage{xcolor} % Import des couleurs dans les textes
\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry} % Marges
\usepackage{parskip} % Saut de ligne
\definecolor{violet}{RGB}{110,30,120} % Mes couleurs perso
\definecolor{prune}{RGB}{161,0,107}
\definecolor{framboise}{RGB}{205,0,55}
\definecolor{orange}{RGB}{224,82,6}
\definecolor{jaune_safran}{RGB}{255,182,18}
\title{xcolor\\ schrek.fr}
\author{Christophe }
\date{Juin 2023}
\begin{document}
\maketitle
\section*{Introduction}

\color{red}
Texte en rouge.
 
\color{blue}
Texte en bleu.

\color{black}
Texte en noir.
\section*{Dans un texte}
Lorem ipsum dolor sit amet, \textcolor{framboise}{consectetur adipiscing elit}, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

\section*{Surlignage}
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute \colorbox{jaune_safran}{irure dolor in reprehenderit} in voluptate velit esse  \colorbox{violet}{\textcolor{white}{cillum dolore eu fugiat nulla pariatur.}}

\section*{Boites}

\fcolorbox{red}{white}{$ \sqrt[4]{x^3} = |x| $} \par


\fcolorbox{red}{white}{
\parbox{0.2\textwidth}{
\begin{itemize}
\item Pommes
\item Poires
\item Abricots
\end{itemize}}
} \par

\fcolorbox{blue}{white}{
\parbox{0.2\textwidth}{ %parbox pour faire une boite
\begin{enumerate}
\item Voitures
\item Trains
\item Vélos
\end{enumerate}}
}
\end{document}

{{< /highlight >}}

{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/cdcjpcgykysq" icone="forward" >}}

{{< bandeau success >}} Pour changer la couleur de la page *\pagecolor{black}* (à placer dans l'entête). {{< / bandeau >}} 


## Liens
https://www.ctan.org/pkg/xcolor

https://www.lesfichesabebert.fr/TeX/latex/Couleur.html

https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX

https://calque.pagesperso-orange.fr/latex/latexps.html

{{< chat cactus-comments >}}
