---
title: "Les fichiers Parquet"
date: 2024-05-29
draft: false
tags: ["Python","Pandas","Parquet"]
categories: ["Linux"]
series: ["Pandas"]
Image: "parquet.webp"
toc: true
---
{{< figure src="parquet.webp" title="" width=200px class="imagearticle" >}}

Les fichiers Parquet sont un format de stockage de données colonnaires open source, souvent utilisé dans le domaine du Big Data et de l'analyse de données. Ils sont conçus pour être efficaces en termes de stockage et de traitement, ce qui les rend adaptés à des volumes de données importants. Voici quelques points clés sur les fichiers Parquet :

- **Compression**: Les fichiers Parquet utilisent des techniques de compression pour réduire la taille des données, ce qui permet d'économiser de l'espace de stockage et de réduire les temps de transfert sur le réseau.

- **Colonnes**: Contrairement aux formats de fichier traditionnels qui stockent les données par lignes, Parquet stocke les données par colonnes. Cela permet une lecture sélective efficace des données, ce qui peut accélérer les requêtes analytiques, car seules les colonnes nécessaires sont lues.

-  **Partitions**: Les fichiers Parquet peuvent être partitionnés, ce qui signifie qu'ils peuvent être divisés en sous-groupes basés sur les valeurs de certaines colonnes. Cela peut améliorer les performances lors de l'exécution d'opérations de filtrage ou d'agrégation, car seules les partitions pertinentes sont traitées.

- **Schéma**: Les fichiers Parquet incluent un schéma intégré qui spécifie la structure des données stockées dans le fichier. Cela permet de garantir l'intégrité des données et facilite la lecture des données sans avoir besoin d'informations externes sur la structure.

En résumé, les fichiers Parquet sont un format de stockage de données efficace, conçu pour répondre aux besoins des applications analytiques sur des ensembles de données volumineux.

# Installation 

```python
$ pip install  pyarrow

```

'''

## Exemple 

{{< include-html "Parquet.html" >}}


## Liens 
https://parquet.apache.org/

https://fr.wikipedia.org/wiki/Apache_Parquet

https://www.icem7.fr/cartographie/parquet-devrait-remplacer-le-format-csv/

https://www.cetic.be/Apache-Parquet-pour-le-stockage-de-donnees-volumineuses
