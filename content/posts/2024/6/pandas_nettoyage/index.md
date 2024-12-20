---
title: "Pandas- nettoyage des données"
date: 2024-06-15
draft: false
tags: ["Python","Pandas"]
categories: ["Linux"]
series: ["Pandas"]
Image: "pandas.webp"
toc: true
---
{{< figure src="pandas.webp" title="" width=200px class="imagearticle" >}}

Le nettoyage des données est une étapes cruciale dans le processus d'analyse de données, car les données brutes peuvent contenir des erreurs, des valeurs manquantes et d'autres problèmes qui peuvent affecter les résultats de l'analyse.

La bibliothèque Pandas en Python est un outils puissant pour le nettoyage des données, offrant de nombreuses méthodes utiles pour préparer les données pour l'analyse.

## L'import des données 

```python
df = pd.read_csv("data.csv",skiprows=3, skipfooter=2)

```
- skiprows: va permettre de ne pas tenir compte des premières ligne du fichier.
- skifooter: ne pa tenir compte des dernières ligne.


## Affichage des infos 

La methode .info(), va nous retourner toutes les information du dataframe.

```python
>>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   prenom     500 non-null    object
 1   nom        500 non-null    object
 2   telephone  500 non-null    object
 3   couleur    500 non-null    object
 4   courriel   500 non-null    object
 5   ip         500 non-null    object
dtypes: object(6)
memory usage: 23.6+ KB

```
Head va permetre d'afficher une partie des données

```python
>>> print(df.head)
<bound method NDFrame.head of       prenom           nom  ...                        courriel               ip
0      Jalon     Greenholt  ...    Felicia.Emmerich28@yahoo.com    248.90.138.87
1       Jose     VonRueden  ...     Lane_Williamson28@gmail.com  210.108.210.101
2      Emmet         Fahey  ...    Andreanne_Schiller@gmail.com   87.132.186.167
3      Jamie          Ryan  ...   Alverta_Dickinson69@yahoo.com     172.4.34.241
4    Aurelie        Parker  ...             Bryce55@hotmail.com  139.217.236.254
..       ...           ...  ...                             ...              ...
495   Norris      Lindgren  ...    Tomasa_Stroman29@hotmail.com      1.8.192.224
496     Nico          Batz  ...           Makayla80@hotmail.com     133.44.36.27
497  Cordell     Dickinson  ...             Lonzo65@hotmail.com  109.118.198.103
498   Alfred  Pfannerstill  ...            Eugene24@hotmail.com  157.127.101.189
499   Darien      Shanahan  ...  Sylvester.Predovic63@gmail.com   216.106.145.64

[500 rows x 6 columns]>
```


## Traitement des colonnes
Dans certain cas, on va devoir renommer, supprimer ou redefinir le type des colonnes.

- Renommer les colonnes.
```python
>>> df.columns = ['id','periode','voyage','demande','em','type','date']
```

- Supprimer une colonne.

```python
>>> del df['ip']
```
- Supprimer plusieurs colonnes.

```python
>>> df1= df.drop(columns=["prenom","nom"])
>>> df1.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   telephone  500 non-null    object
 1   couleur    500 non-null    object
 2   courriel   500 non-null    object
dtypes: object(3)
memory usage: 11.8+ KB

```



## Liens
https://www.osedea.com/fr/blogue/nettoyage-donnees-python-pandas

https://www.delftstack.com/fr/api/python-pandas/

https://openclassrooms.com/fr/courses/7410486-nettoyez-et-analysez-votre-jeu-de-donnees/7451506-nettoyez-vos-donnees-avec-python


