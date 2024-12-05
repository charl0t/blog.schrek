---
title: "Gestionnaire de fichier Caja"
date: 2024-03-25
draft: false
tags: ["Linux","Caja"]
categories: ["Linux"]
Image: "caja.webp"
toc: true
---
Caja est le gestionnaire de fichiers officiel de l'environnement MATE. 


## Script 
Je voulais ajouter des possibilités de click droit via des scripts. 

C’est assez simple, il suffit de placer une exécutable dans le dossier *./config/caja/script* de votre répertoire */home*.

<!--more-->

## Variables

Quelques variables pour utiliser les scripts.

{{< highlight bash  >}}
*$@* Fichiers sélectionnés 

*$PWD* Répertoire courant 

*$CAJA_SCRIPT_SELECTED_FILE_PATHS*  
Chemin des fichiers sélectionnés.

*$CAJA_SCRIPT_SELECTED_URI* 
URI des fichiers sélectionnés, pour les fichiers distants.

*$CAJA_SCRIPT_CURRENT_URI*   
URI du dossier depuis lequel le script est lancé.
{{< /highlight >}}


Astuce: Dans le cas de multiples sélections, les chemins/URI sont séparés par des retours à la ligne.

On va tester dans un script en créant un fichier *test* dans le dossier *.config/caja/script*.


{{< highlight bash  >}}
#!/bin/bash
exec &>> "$(basename "$0").log"
echo "\$@=$@"
echo "\$1=$1"
echo
echo "PWD=$PWD"
echo "$CAJA_SCRIPT_SELECTED_FILE_PATHS"
echo "$CAJA_SCRIPT_SELECTED_URI" 
echo "$CAJA_SCRIPT_CURRENT_URI"
{{< /highlight >}}

Il faut autoriser l'exécution.

{{< highlight bash  >}}
$ chmod +x test
{{< /highlight >}}

Avec caja, on fait  un clic droit sur un fichier et on obtient un fichier *test.log*

{{< highlight bash  >}}
$@=checksum
$1=checksum
PWD=/home/tuxien/.config/caja/scripts
/home/tuxien/.config/caja/scripts/checksum
file:///home/tuxien/.config/caja/scripts
{{< /highlight >}}

## Exemple de script 
On va convertir des images au format [Webp](https://fr.wikipedia.org/wiki/WebP) (j'utilise ce format pour mes articles dans Hugo) en utilisant le langage Python.

Toujours dans le dossier de travail *.config/caja/script/*.

{{< highlight python  >}}
#!/usr/bin/python3

import os
import sys

def new_name(file):
    os.path.splitext(file)
    return '.'.join([os.path.splitext(file)[0],'webp'])

files = sys.argv[1:]

for file in files:
    os.system('cwebp -q 90 %s -o %s' % (file, new_name(file)))
{{< /highlight >}}

Quelques scripts en PJ, bien regarder les dépendances comme *zenity* pour afficher des infos.

{{< pj />}}

## Liens

https://doc.ubuntu-fr.org/caja

https://gist.github.com/bitsgalore/fc69e55c67830413f97c

https://www.pragmageek.fr/2022/01/la-bonne-maniere-de-faire-un-script-nautilus-en-bash/

https://community.linuxmint.com/software/view/caja
