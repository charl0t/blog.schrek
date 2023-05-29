---
title: "Lier Framacarte a Framacalc"
date: 2023-03-23
draft: false
tags: ["Carte","Framacarte"]
categories: ["Web"]
image: "umap_logo.webp"
toc: true
---
{{< figure src="umap_logo.webp" title="" width=200px class="imagearticle" >}}

Il peut être pratique de lier une feuille de tableur avec une carte pour mieux gérer les points .
Avec [Framacarte](https://framacarte.org) et [Framacalc](https://lite.framacalc.org) c’est possible.
Sur le [Wiki](https://wiki.cartocite.fr/doku.php?id=umap:tutoriel_umap) de Cartocité on trouve plein de ressource sur le sujet.


## Créer et configurer le tableur

On va sur [Framacalc](https://lite.framacalc.org) pour créer notre tableur.
- Sur la 1ᵉʳ colonne on va mettre la latitude en ajoutant "lat" (case A1 sans les guillemets)
- 2ᵉ colonne, la longitude  "lon"  (case B1 sans les guillemets)
- 3ᵉ colonne, le nom  "nom"  (case C1 sans les guillemets)
- 4ᵉ colonne, description "description"  (case D1 sans les guillemets)

Pour l’exemple on va prendre les arènes d’Arles. 
https://www.openstreetmap.org/#map=19/43.67773/4.63103
L’URL nous indique le niveau de zoom, la latitude et la longitude. On récupère les données pour remplir notre tableau.

{{< figure src="capture_du_2023-03-22_18-06-35-cdedc.webp" title="" width=600px class="imagearticle" >}}

## La carte
Après avoir créé un compte sur [Framacarte](https://framacarte.org), on ouvre une nouvelle carte et on lui donne un nom.
En haut à droite, on clique sur le crayon pour éditer la carte et on ajoute un calque que l’on nomme Arles.
Ensuite dans données distante on colle le lien du calque en ajoutant a la fin ".csv " (sans les guillemets)
Exemple: https://lite.framacalc.org/kqqbsdezeyd2h-9zz4.cvs
On active Dynamique dessous. 

{{< figure src="capture_du_2023-03-22_18-14-29-4cc4b.webp" title="" width=400px class="imagearticle" >}}

A partir de là on doit avoir une icône qui apparaît sur les arènes 

Dans les options d’interaction du calque on modifie: 
- Forme du popup  "grande".
- Gabarie du contenu du popup.

{{< highlight bash >}}
# {nom}
[[{description}]]
{{< / highlight >}}

{{< figure src="capture_du_2023-03-22_18-24-42-d494b.webp" title="" width=400px class="imagearticle" >}}

## Explication

{{< highlight bash >}}
- # {nom}, # c est pour dire que c est un titre, {nom} va chercher les données dans la colonne "nom" du tableur.
{{< / highlight >}}

Vous pouvez retrouver le code de mise en forme en cliquant sur le ? 


{{< figure src="capture_du_2023-03-22_18-29-17-409b0.webp" title="" width=600px class="imagearticle" >}}

On enregistre et on désactive l’édition pour voir le résultat.
https://framacarte.org/fr/map/test1_149229

J ai rajouté une colonne image avec l’URL d’une image et le tag dans les options (200 pour la taille de l’image) d’interaction.

{{< highlight bash >}}
{{{image}|200}}
{{< / highlight >}}

## Pour finir
Umap propose plein de possibilité, je vous renvoie sur le [Wiki](https://wiki.cartocite.fr/doku.php?id=umap:tutoriel_umap) de Cartocité qui est très complet. 

## Liens
https://framacarte.org/fr/map/test1_149229#15/43.6786/4.6349

https://www.openstreetmap.org/#map=18/43.67685/4.63006

{{< chat cactus-comments >}}
 
