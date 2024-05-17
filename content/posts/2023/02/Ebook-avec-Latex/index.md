---
title: "Ecrire un ebook avec Latex"
date: 2023-02-03
draft: false
tags: ["Ebook"]
categories: ["Latex"]
series: ["Latex"]
image: "epub.wepb"
toc: true
---
{{< figure src="epub.wepb" title="" width=200px class="imagearticle" >}}

{{< bandeau success >}} MaJ 29/05/2023 Ajout d'un livre "LaTeX pour litteraires"(Éric Guichard), bouton overleaf.com{{< / bandeau >}} 

J’avais l’idée d’écrire un petit livre sur la Rome antique, une histoire d’un soldat romain qui devient un pirate.
Au début j’étais partie sur LibreOffice Writer, mais je me suis vite retourné vers Latex.
Pour organiser mes idées et structurer le document j’ai utilisé cette structure.
Vous trouverez les sources en bas de l’article.

J’ai aucun talent littéraire merci d’être indulgent.

## Organisation des fichiers 
{{< figure src="organisation_livre-cc1fc.webp" title="" width=200px class="imagearticle" >}}

Code Latex de la page principale :

J’ai utilisé la fonction \include pour ajouter des fichiers externes .

{{< highlight tex >}}
    \documentclass[11pt,a4paper,oneside]{book} % taille de police, taille papier, recto, classe livre
    \usepackage[utf8]{inputenc} % Encodage
    \usepackage[french]{babel} % Utilisation du français
    \usepackage[T1]{fontenc} % Les mots accentués
    \usepackage{lmodern} % Police de caractère
    \usepackage{hyperref} % Lien http
    \usepackage{graphicx} % Pour inserer des images
    \pagestyle{empty} % page vide
    \author{Schrek christophe}
    \title{''Le pirate de Rome''}
    \author{''Schrek christophe''}
    \date{\today}
     
    \begin{document}
    \maketitle %Titre
    \tableofcontents %Table des matieres
    \include{notes} % on inclue note.tex
    \include{personnages} % on inclue personnages.tex
    \include{chap1/chapitre1}
    \include{chap2/chapitre2}
    \include{chap3/chapitre3}
    \include{chap4/chapitre4}
    \include{chap5/chapitre5}
    \include{chap6/chapitre6}
    \include{chap7/chapitre7}
    \end{document}
{{< / highlight >}}

[Télécharger](latex.txt)

Code Latex des chapitres :

{{< highlight Tex >}}
    \chapter{Le départ}
    %Notes:
    %Origine du hero + Situation empire romain
    %Compagnons
    %route pour le camp d’entraînement
    %Sources
    %http://fr.wikipedia.org/wiki/Troupes_auxiliaires
    %http://latin.collegejeanjaures-cransac.org/legionrom.htm
     
    \section{La veille}
    La nuit a était courte, j'ai trop fait la fête dans le quartier de Subure \footnote{\href{https://fr.wikipedia.org/wiki/Subure}{Subure ou Suburre (Subūra en latin) est un quartier pauvre et populeux de la Rome antique.}}
    \medskip
    %avec mes amis. On s’était donné rendez-vous prêt de la fontaine pour manger et boire mais ça a vite dérape.
    %https://www.histoire-en-questions.fr/antiquite/rome-vie-tavernes.html
    %https://anticopedie.fr/WordPress/?p=431 
     
    En fin d’après midi, direction la popina\footnote{Taverne de mauvaise réputation} de Bilius, un vieux et gros Gaulois plein de cicatrices qui dirige cet établissement de "caractère".
    C'est grâce a lui que j'ai pu gagner un peu d'argent en nettoyant tous les matins la taverne des restes de la veille.
    \medskip
{{< / highlight >}}

[Télécharger](latex2.txt)

{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/jsbppgfsrxrw" icone="forward" >}}

## Création de l’Epub
J’ai utilisé Tex4ebook qui génère un Epub propre (pour mon cas).

{{< highlight bash >}}
$ tex4ebook -d epub/ -f epub3 intro.tex
{{< / highlight >}}

[Télécharger](intro.epub)

Pour les options :

{{< highlight bash >}}
-d epub/   dossier de sortie
-f epub3  version 3 du format epub 
{{< / highlight >}}


## Le résultat 
J’ai vérifié le résultat avec [EpubCheck](https://www.w3.org/publishing/epubcheck/):

{{< highlight bash >}}
$ java -jar epubcheck.jar intro.epub 
Vérifications faites en utilisant les règles de la version epub 3.3.
Aucune erreur ou avertissement détecté.
Messages: 0 fatale / 0 erreur / 0 avertissement / 0 info
EPUBCheck terminé
{{< / highlight >}}


## Les sources:

[Télécharger](latex_pirates.zip)

{{%pj /%}}





