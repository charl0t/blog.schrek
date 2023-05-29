---
title: "Latex, PDF éditable"
date: 2023-08-10
draft: false
tags: ["Latex","Pdf","hyperref"]
categories: ["Latex"]
series: ["Latex"]
image: "latex_logo.webp"
toc: true
---
Avec la classe *[hyperref](https://ctan.org/pkg/hyperref)*, on peut facilement créer des documents PDF éditable.

J'ai fait un petit exemple avec un attestation d'hébergement.

La [documentation](https://texlive.mycozy.space/macros/latex/contrib/hyperref/doc/hyperref-doc.html#x1-590009) est bien faite.

<!-- more -->

## Exemple
{{< highlight tex >}}
\documentclass[12pt,a4paper]{article}
\usepackage[right=2cm,left=2cm,top=2cm,bottom=2cm]{geometry}
\usepackage[french]{babel}
\usepackage[default]{lato}
\usepackage{xcolor}
\usepackage{hyperref}
	\hypersetup{
		colorlinks=true,
		linkcolor=black,
	}
\usepackage{fancyhdr}
\pagestyle{empty}

\setlength\parindent{0pt}

\begin{document}

\begin{Form}

\begin{center}
	\textbf{\uppercase{ATTESTATION D'HÉBERGEMENT}} \\
\end{center}
\vspace{5mm}
Je soussigné(e), \\

\vspace{5mm}

\TextField[width=5cm,borderwidth=0pt]{Mme/M. :} \\
\TextField[width=5cm,borderwidth=0pt]{Né(e) le :} \\
\TextField[width=5cm,borderwidth=0pt]{À :} \\
\TextField[width=14cm,borderwidth=0pt]{Demeurant :} \\

\vspace{5mm}

déclare sur l'honneur héberger à mon domicile,\\

\vspace{5mm}
\TextField[width=5cm,borderwidth=0pt]{Mme/M. :} \\
\TextField[width=5cm,borderwidth=0pt]{Né(e) le :} \\
\TextField[width=5cm,borderwidth=0pt]{À :} \\
\vspace{5mm}

depuis le\\

\vspace{5mm}

\TextField[width=8cm,borderwidth=0pt]{Date de début d'hébergement:}\\
\vspace{5mm}
\TextField[width=14cm,borderwidth=0pt]{à l'adresse suivante :}

\TextField[width=8cm,borderwidth=0pt]{Fait à :} \\
\\
\TextField[width=4cm,borderwidth=0pt]{Le :} 
\TextField[width=1cm,borderwidth=0pt,maxlen=2]{à} 
\TextField[width=1cm,borderwidth=0pt,maxlen=2]{h} \\


\TextField[width=14cm,borderwidth=0pt]{Signature :} 

\end{Form}

\end{document}
{{< /highlight >}}

{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/dgnpzyngzbqk" icone="forward" >}}

## Explications

- On ouvre le formulaire avec la balise *\begin{Form}*
- *\TextField[width=4cm,borderwidth=0pt]{Le :}* Ajoute la partie à completer
- On ferme le formulaire avec la balise *\end{Form}*

## En vrac
Voir en bas dans les liens de [téléchargements]({{< ref "#liens" >}}).

{{< highlight tex >}}
\documentclass[12pt,a4paper]{article}
\usepackage[right=2cm,left=2cm,top=2cm,bottom=2cm]{geometry}
\usepackage[french]{babel}
\usepackage[default]{lato}
\usepackage{xcolor}
\usepackage{hyperref}
	\hypersetup{
		colorlinks=true,
		linkcolor=black,
	}
\usepackage{fancyhdr}
\pagestyle{empty}

\begin{document}


\begin{Form}
Case à cocher:\\

	\CheckBox[bordercolor=black]{}


Villes:\\ 

\ChoiceMenu[combo,width=5cm,charsize=12pt,default=Paris,bordercolor=blue]{\mbox{}}{Paris,Lyon,Marseille} \\

Sexe:\\


\ChoiceMenu[radio,charsize=14pt,bordercolor=green,radiosymbol=\ding{170}]{\mbox{}}{Homme,Femme,Aucun}\\

Études:\\

\CheckBox[charsize=12pt]{Rien:}\\

\CheckBox[charsize=12pt]{Collège:}\\

\CheckBox[charsize=12pt]{Lycée:} \\
\end{Form}

\end{document}
{{< /highlight >}}

## Astuce
Pour modifier l'icône de choix *\ding{170}]* , voir liste dessous ou sur [Cpan](https://ctan.org/pkg/pifont):

{{< figure src="ding.webp" title="" width=500px class="imagearticle" >}}

## Liens
https://blog.dorian-depriester.fr/latex/creer-des-formulaire-pdf-editables

https://la-bibliotex.fr/2020/04/11/creer-des-pdf-editables-avec-latex/

https://www.maltegerken.de/blog/2021/07/creating-pdf-forms-with-latex/

https://latex-tutorial.com/bullet-styles/

{{< pj />}}


{{< chat cactus-comments >}}
