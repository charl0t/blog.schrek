---
title: "Pandas, importer un fichier csv"
date: 2024-05-10
draft: false
tags: ["Python","Pandas"]
categories: ["Linux"]
series: ["Pandas"]
Image: "pandas.webp"
toc: true
---

J’avais besoin de traiter des fichiers CSV pour en extraire des données. J’ai commencé à faire cela avec un tableur, mais comme je suis feignant,je voulais automatiser tout cela.

## Le csv
Je dois:
- Importer le fichier CSV
- Nettoyer des données inutiles
- Mettre en forme des colonnes
- Extraire des données

<!--more-->

## Au travail.
Pour faire tous ça je vais utiliser le langage Python avec la bibliothèque [Pandas](https://fr.wikipedia.org/wiki/Pandas)

{{< highlight python >}}
#!/usr/bin/python
import pandas as pd
df = pd.read_csv('journal.csv',sep = ';',skiprows = 3 ,encoding='ISO-8859-1')
df = df.drop(columns=['Offre', 'Flotte','Entreprise','Code mission','Région'])
df.rename(columns = {'Date de désactivation':'Desactivation','Téléphone':'Numero'},inplace = True)
df.info()
df.to_csv('df.csv', index=False)
{{< /highlight >}}


- sep --> separateur
- skiprows --> On supprime les 3 premieres lignes
- encoding --> j'ai du changer l encodage du texte
- df.drop --> On supprime les colonnes inutiles
- df.rename --> Renomage de certaines colonnes
- df.info() --> On affiche les infos 
- df.to_csv --> Exporte les données 



## Liens

https://pandas.pydata.org

https://jhub.cnam.fr/doc/notebooks/Manipulations_de_donnees_Python_Pandas.html

https://github.com/adamerose/PandasGUI

https://github.com/guipsamora/pandas_exercises/tree/master

https://markbdsouza.github.io/csv-data-generator/

https://github.com/jhroy/tuto-pandas


