---
title: "Publipostage avec Koma-Script"
date: 2023-09-20
draft: false
tags: ["Latex","Koma-Script","Publipostage","scrlttr2"]
categories: ["Latex"]
series: ["Latex"]
image: "publi.webp"
toc: true
---
On veut réaliser du publipostage, envoyer la même lettre à plusieurs destinataires.

Avec notre modèle de lettre déjà fait, on va y ajouter un carnet d'adresse, et générer plusieurs lettres.

<!--more-->

## Le fichier des adresses

Création du fichier *adresses.adr*

{{< highlight tex >}}
\adrentry{Dupont}{Michel}{12 rue des poules\\13200 Arles}{06 55 22 12 17}{h}{}{}{}{DUPONT}
\adrentry{Miron}{Elsa}{20 chemin des biches\\13200 Arles}{06 88 99 88 55}{f}{}{}{}{MIRON}
\adrentry{Tarion}{René}{1bis route bleue\\13130 Miramas}{07 15 25 63 52}{h}{}{}{}{TARION}
{{< /highlight>}}



## Le fichier de la lettre

{{< highlight tex >}}
\begin{document}
\renewcommand*{\adrentry}[9]{%
\begin{letter}{#1 #2 \\#3}
    \if #5h \opening{Monsieur,} \fi
    \if #5f \opening{Madame,} \fi
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

\end{letter}
}
\input{adresses.adr}
{{< /highlight>}}


{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/qbpwtcssrqhk" icone="forward" >}}


## Fichiers
{{< pj />}}

## Liens
https://www.ctan.org/pkg/scrlttr2

https://www.ctan.org/pkg/koma-script

https://framalibre.org/content/koma-script





