---
title: "Nano"
date: 2023-03-23
draft: false
tags: ["Nano"]
categories: ["Linux"]
image: "nano.webp"
toc: true
---
{{< figure src="nano.webp" title="" width=200px class="imagearticle" >}}

Un éditeur de fichier très simple.

## Pour ouvrir un fichier 

{{< highlight bash >}}
$ nano  index.html
{{< / highlight >}}

## Créer un fichier 

{{< highlight bash >}}
$ nano  fichier.txt
{{< / highlight >}}

## Les raccourcis courants 

{{< highlight bash >}}
 ctrl + G ...... Appeler le menu d’aide
 ctrl + X ...... Fermer et, le cas échéant, quitter nano
 ctrl + O ...... Écrire le fichier en cours sur le disque
 ctrl + J ...... Justifier le paragraphe courant
 ctrl + R ...... Insérer un autre fichier dans le fichier en cours
 ctrl + W ...... Rechercher une chaîne dans l’éditeur
 ctrl + Y ...... Aller à l’écran précédent
 ctrl + V...... Aller à l’écran suivant
 ctrl + K ...... Couper la ligne courante vers le presse-papiers
 ctrl + U ...... Coller le presse-papiers à partir de la ligne courante
 ctrl + C ...... Indiquer la position du curseur
{{< / highlight >}}

## Coloration syntaxique

J’ai trouvé un petit script sympa [ici](https://github.com/scopatz/nanorc)  qui modifie le nanorc(fichier de configuration) pour avoir un peu de couleurs .

{{< highlight bash >}}
$ curl https://raw.githubusercontent.com/scopatz/nanorc/master/install.sh | sh nanorc
{{< / highlight >}}

En modifiant le fichier de configuration de Nano, on peut ajouter des possibilités.

{{< highlight bash >}}
$ nano ~/.nanorc
{{< / highlight >}}

Si on modifie le fichier /etc/nanorc, les modifications s’appliqueront à tous les utilisateurs.

Quelques exemples :

 Indentation automatique : set autoindent

 Sauvegarde automatique : set backup

 Active l’utilisation de la souris : set mouse

Plus d’infos [ici](http://pwet.fr/man/linux/formats/nanorc/).


## Liens

https://www.nano-editor.org/

https://github.com/scopatz/nanorc

http://pwet.fr/man/linux/formats/nanorc/

https://debian-facile.org/doc:editeurs:nano


{{< chat cactus-comments >}}
