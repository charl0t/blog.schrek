---
title: "Pandas et les structures"
date: 2024-05-03
draft: false
tags: ["Python","Pandas"]
categories: ["Linux"]
series: ["Pandas"]
Image: "pandas.webp"
toc: true
---
{{< figure src="pandas.webp" title="" width=200px class="imagearticle" >}}

La bibliothèque Pandas fournit deux structures de données principales pour manipuler des données structurées : les séries et les dataframes.

## Les séries
Une série est un tableau unidimensionnel de données homogènes, indexé par des étiquettes. Les étiquettes peuvent être de n'importe quel type (chaînes de caractères, entiers, dates, etc.), ce qui permet de manipuler des données de manière flexible. Les séries peuvent être créées à partir de listes, de tableaux NumPy, de dictionnaires ou d'autres structures de données.

## Les dataframes
Un dataframe est un tableau bidimensionnel de données hétérogènes, composé de lignes et de colonnes. Les colonnes peuvent être de types différents (chaînes de caractères, entiers, flottants, etc.), ce qui permet de stocker des données de différents types dans une seule structure de données. Les lignes sont indexées par des étiquettes, tout comme les séries. Les dataframes peuvent être créés à partir de dictionnaires, de listes de dictionnaires, de tableaux NumPy, de fichiers CSV, de bases de données SQL, etc.

Les séries et les dataframes sont conçus pour fonctionner ensemble de manière transparente. Par exemple, il est possible d'extraire une colonne d'un dataframe sous la forme d'une série, ou d'appliquer une opération sur chaque élément d'une série ou d'un dataframe à l'aide de fonctions d'application vectorisées.

## En résumé
Les séries et les dataframes sont les structures de données principales de la bibliothèque Pandas pour manipuler des données structurées. Les séries sont des tableaux unidimensionnels indexés par des étiquettes, tandis que les dataframes sont des tableaux bidimensionnels composés de lignes et de colonnes, indexés par des étiquettes. Les séries et les dataframes sont conçus pour fonctionner ensemble de manière transparente, offrant ainsi une grande flexibilité pour manipuler et analyser des données structurées.

## Liens
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html

http://www.python-simple.com/python-pandas/creation-series.php

https://cdiese.fr/pandas-series/

