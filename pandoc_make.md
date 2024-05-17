


La commande make est un utilitaire de ligne de commande qui permet d'automatiser la compilation et la construction de projets logiciels. Cependant, dans le contexte de Pandoc, make est souvent utilisé pour automatiser la conversion de fichiers de différents formats à l'aide de Pandoc.

Pandoc est un outil de conversion de documents qui permet de convertir des fichiers de différents formats, tels que Markdown, HTML, PDF et Microsoft Word, entre autres. Pour convertir un fichier à l'aide de Pandoc, vous pouvez utiliser une commande de ligne de commande telle que :pandoc input.md -o output.pdf
Cette commande convertit le fichier input.md en format Markdown en un fichier output.pdf en format PDF.

Cependant, si vous avez de nombreux fichiers à convertir ou si vous devez effectuer plusieurs étapes de conversion, l'utilisation de la commande make peut simplifier le processus. Par exemple, vous pouvez créer un fichier Makefile qui contient des règles pour la conversion de fichiers à l'aide de Pandoc. 

Voici un exemple de fichier Makefile:
```
# Nom du fichier source
SRC = document.md

# Nom du fichier de sortie
OUT = document.pdf

# Commande pour convertir le fichier md en PDF avec PANDOC
$(OUT): $(SRC
	pandoc $(SRC) -o $(OUT)
```


Pour utiliser ce fichier *Makefile*, vous pouvez simplement exécuter la commande make dans le répertoire où se trouve le fichier *Makefile*. La commande make lira le fichier Makefile et exécutera les règles appropriées pour générer les fichiers spécifiés.

La commande make est souvent utilisée avec Pandoc pour automatiser la conversion de fichiers de différents formats. En créant un fichier Makefile contenant des règles pour la conversion de fichiers, vous pouvez simplifier le processus de conversion et gagner du temps.

## Liens
https://makefiletutorial.com/

https://www.arthurperret.fr/cours/pandoc.html

https://www.arthurperret.fr/blog/2022-06-22-publication-multiformats-pandoc-make.html

https://gitlab.com/cestabrupt/gabarit-abrupt
