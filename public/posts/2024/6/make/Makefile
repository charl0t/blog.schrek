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
