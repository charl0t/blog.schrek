---
title: "Latex de la couleur dans vos codes"
date: 2023-09-01
draft: false
tags: ["Latex","minted"]
categories: ["Latex"]
series: ["Latex"]
image: "minted.webp"
toc: true
---
Le module [*minted*](https://ctan.org/pkg/minted) permet de coloriser vos codes.

Minted utilise [Pygments](https://pygments.org/languages/) pour ajouter de la couleurs, vous trouverez la liste des codes supportés sur le site.

Il y a aussi differents [styles](https://pygments.org/styles/)

## Utilisation
{{< highlight tex >}}
\begin{minted}[Option]{Language}
Code
\end{minted}
{{< /highlight>}}

Exemple:
{{< highlight tex >}}
\section{Python}
\begin{minted}[style=fruity,bgcolor=black]{python}
print('Hello, World!')
\end{minted}
\end{document}
{{< /highlight >}}

## Les options
- style : Changer le [style](https://pygments.org/styles/);
- linenos : Activer les numerotations des lignes;
- numbers: Côté la numérotation est affichée (left, right ou both pour l’afficher des deux côtés);
- firstnumber: changer le debut de numerotation;
- bg : Couleur de fond;
- label: Titre;
- labelposition: Position du titre (none | topline | bottomline | all);
- frame: ligne d'encadrement (none | topline | bottomline | all);
- framesep: Epaisseur des traits (framesep=2mm).


Toutes les options dans la [documentation](https://ctan.org/pkg/minted).


{{< bouton titre="Voir sur overleaf" url="https://fr.overleaf.com/read/hhqnbnqbfzxj" icone="forward" >}}

## Liens
https://ctan.org/pkg/minted

https://fr.overleaf.com/learn/latex/Code_Highlighting_with_minted

https://zestedesavoir.com/tutoriels/1848/presenter-du-code-source-dans-un-document-latex/

{{< chat cactus-comments >}}
