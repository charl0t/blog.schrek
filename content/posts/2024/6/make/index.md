---
title: "Make, génération de fichiers"
date: 2024-06-20
draft: false
tags: ["Make","Markdown"]
categories: ["Linux"]
Image: "make.webp"
toc: true
---


La commande make est un utilitaire de ligne de commande qui permet d'automatiser la compilation et la construction de projets logiciels. Cependant, dans le contexte de Pandoc, make est souvent utilisé pour automatiser la conversion de fichiers de différents formats à l'aide de Pandoc.

Pandoc est un outil de conversion de documents qui permet de convertir des fichiers de différents formats, tels que Markdown, HTML, PDF et Microsoft Word, entre autres. Pour convertir un fichier à l'aide de Pandoc, vous pouvez utiliser une commande de ligne de commande telle que :pandoc input.md -o output.pdf
Cette commande convertit le fichier input.md en format Markdown en un fichier output.pdf en format PDF.

Cependant, si vous avez de nombreux fichiers à convertir ou si vous devez effectuer plusieurs étapes de conversion, l'utilisation de la commande make peut simplifier le processus. Par exemple, vous pouvez créer un fichier Makefile qui contient des règles pour la conversion de fichiers à l'aide de Pandoc. 
Voici un exemple de fichier:
``` c
# Nom du fichier d'entrée
SRC := pandoc_make.md

# Nom du fichier de sortie
OUT := document.pdf

# Commande pour convertir le fichier md en PDF avec PANDOC
all:
	pandoc $(SRC) -o $(OUT)

# Règle pour nettoyer les fichiers
clean:
	rm -rf $(OUT)

```
Pour utiliser ce fichier Makefile, vous pouvez simplement exécuter la commande make dans le répertoire où se trouve le fichier Makefile. La commande make lira le fichier Makefile et exécutera les règles appropriées pour générer les fichiers spécifiés.

Dans cet exemple, on indique que le fichier *document.pdf* doit être généré. La commande *all* indique comment générer ces fichiers à partir du fichier pandoc_make.md à l'aide de Pandoc. 

La règle *clean* permet de supprimer les fichiers générés.

## Plusieurs types de sortie

On reprend l'exemple du dessus

``` c
# Nom du fichier d'entrée
SRC := pandoc_make.md

# Nom du fichier de sortie
OUTPDF := document.pdf
OUTHTML := document.html

.PHONY: all pdf html clean

# Commande pour tous convertir
all: pdf html

# Commande pour convertir le fichier md en PDF avec PANDOC
pdf : $(SRC)
	pandoc $(SRC) -o $(OUTPDF)

# Commande pour convertir le fichier md en HTML avec PANDOC
html : $(SRC)
	pandoc $(SRC) -o $(OUTHTML)

# Règle pour nettoyer les fichiers
clean:
	rm -rf $(OUTPDF)
	rm -rf $(OUTHTML)

```

``` bash
$ make all
pandoc pandoc_make.md -o document.pdf
pandoc pandoc_make.md -o document.html

```

## Plusieurs fichiers sources

``` c
# on va lister les fichiers md dans le dossier md/
SRC = $(sort $(shell find md/ -type f -iname '*.md'))

# Nom du fichier de sortie
OUTPDF := document.pdf
OUTHTML := document.html

.PHONY: all pdf html clean

# Commande pour tous convertir
all: pdf html

# Commande pour convertir le fichier md en PDF avec PANDOC
pdf : $(SRC)
	pandoc -o $(OUTPDF) $(SRC)

# Commande pour convertir le fichier md en HTML avec PANDOC
html : $(SRC)
	pandoc $(SRC) -o $(OUTHTML)

# Règle pour nettoyer les fichiers
clean:
	rm -rf $(OUTPDF)
	rm -rf $(OUTHTML)
```

La commande make est souvent utilisée avec Pandoc pour automatiser la conversion de fichiers de différents formats. En créant un fichier Makefile contenant des règles pour la conversion de fichiers, vous pouvez simplifier le processus de conversion et gagner du temps.


## Liens

https://sites.uclouvain.be/SystInfo/notes/Outils/make.html

https://www.arthurperret.fr/cours/pandoc.html

https://www.arthurperret.fr/blog/2022-06-22-publication-multiformats-pandoc-make.htm

https://gitlab.com/cestabrupt/gabarit-abrupt
