---
title: "Lettre sous latex"
date: 2023-03-28
draft: false
tags: ["Lettre","Latex"]
categories: ["Latex"]
image: "latex_logo-1ee3e.svg"
toc: true
---
{{< figure src="latex_logo-1ee3e.svg" title="" width=200px class="imagearticle" >}}

Utilisation de la classe lettre avec LaTex.

J’ai commenté le code pour plus de clarté.

Petit rajout du tampon fait dans cet article Tampon encreur sous Gimp

En cas d’erreur babel:

{{< highlight bash >}}
sudo apt-get install texlive-lang-french
{{< / highlight >}}

## Le code

{{< highlight tex >}}
    \documentclass[12pt]{lettre} %12p taille lettres (10 et 11 possible), déclaration classe lettre
     
    \usepackage[utf8]{inputenc} % Encodage  
    \usepackage[T1]{fontenc} % Les mots accentués
    \usepackage{lmodern} % Type de police
    \usepackage{eurosym} % Pouvoir écrire le symbole "€"
    \usepackage[french]{babel} % Utilisation du français
    \usepackage{numprint} % Séparateur décimal
    \usepackage{graphicx} % Pour inclure des images
    \begin{document}
    \begin{letter}{Service des râleurs\\66, rue du train\\13200 Arles} % Destinataire
    \basdepage{\pagetotalname{1}}
    \name{Prénom nom}
    \signature{Nom Prénom \includegraphics[width=75px, angle=-45]{tampon.png}} % Si different de l'expediteur a commenter sinon, ajout du tampon
    \location{htextei}
    \address{Prenom Nom \\13, rue du cheval\\13200 Arles}
    \lieu{Arles}
    \date {le 10 mai 2023}                   % Sinon  \nodate
    \lieu{lieu envoi}                       % Sinon \nolieu
    \telephone{01 02 03 04 05}
    \email{prenom.nom@fai.fr}
    \nofax % Pas de fax sinon fax{}
    \Vref{3456678} % Reference du destinataire a commenter sinon
    \Nref{6654334} % Reference de l'envoyeur a commenter sinon
     
    \def\concname{Objet :~} % On définit  l’objet
    \conc{rétractation}
    \opening{Madame, Monsieur,}
     
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum \numprint{2000}~\euro.
     
    \closing{Je vous prie d’agréer, Madame, Monsieur,
    mes salutations distinguées.}
     
    \ps{PS :}{Lorem ipsum dolor sit amet, consectetur adipiscing elit.}
    \cc{Nom des autres destinataires}
    \encl{Pièces jointes}
     
    \end{letter}
     
    \end{document}
{{< / highlight >}}

{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/rtfknsbdvxnt" icone="forward" >}}

Le tampon qui va bien

{{< figure src="tampon.png" title="" width=200px class="imagearticle" >}}

## Résultat

[La Lettre.](lettre.pdf)

## Liens
https://fr.wikibooks.org/wiki/LaTeX/Lettre

https://zestedesavoir.com/tutoriels/508/ecrire-des-lettres-en-latex/

https://www.ctan.org/pkg/lettre




