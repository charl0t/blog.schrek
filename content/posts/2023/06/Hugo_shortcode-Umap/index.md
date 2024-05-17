---
title: "Shortcode Framacarte"
date: 2023-06-25
draft: false
tags: ["Shortcode", "Framacarte","Hugo","Umap"]
categories: ["Web"]
series: ["Hugo"]
image: "umap_logo.webp"
toc: true
---
{{< figure src="umap_logo.webp" title="" width=200px class="imagearticle" >}}

Grace a [Framasoft](https://framacarte.org/fr/), on peut avoir un service pour créer des cartes personnalisées. 
Le service s'appuie sur [Umap](https://github.com/umap-project/umap/).

Il existe un shortecode pour umap sur [GIT](https://github.com/Hanzei/hugo-component-osm), j'ai juste modifié l'URL dans le code.

## Framacarte
Quand on a créer une carte (un super tuto sur [cartocite.fr/](https://wiki.cartocite.fr/doku.php?id=umap:tutoriel_umap)) sur [Framacarte](https://framacarte.org/fr/), on aimerait l'afficher sur notre site.

On peut utiliser l'import de l'iframe.

On clique sur l'icône de partage {{< figure src="partage.webp" alt="partage umap" width=60px  >}}

On récupère le code.
{{< figure src="iframe.webp" alt="iframe umap" width=300px  >}}



## Le code original

{{< highlight html >}}
<iframe width="100%" height="300px" frameborder="0" allowfullscreen src="https//framacarte.org/fr/map/carte-de-france_154547?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false"></iframe><p><a href="https//framacarte.org/fr/map/carte-de-france_154547">Voir en plein écran</a></p>
{{< /highlight >}}

Pour que ça marche, il faut ajouter le fichier de configuration du site (*config.toml*).
{{< highlight toml >}}
[markup.goldmark.renderer]
unsafe = true
{{< /highlight >}}

Des idées sur l'iframe en mode Hugo [ici](https://stackoverflow.com/questions/68036749/embedding-iframe-in-hugo-site).

Sinon il y a les shortcodes.

## Le Shortcode
On va créer dans le dossier des shortcodes */themes/VOTRETHEME/layouts/shortcodes* un fichier frumap.html

{{< highlight go-html-template >}}
{{ $mapName := .Get "mapName" }}

{{ $mapWidth := .Get "mapWidth" | default "100%" }}
{{ $mapHeight := .Get "mapHeight" | default "600px" }}

{{ $scaleControl := .Get "scaleControl" | default "true"  }}
{{ $miniMap := .Get "miniMap" | default "false" }}
{{ $scrollWheelZoom := .Get "scrollWheelZoom" | default "true" }}
{{ $zoomControl := .Get "zoomControl" | default "true" }}
{{ $allowEdit := .Get "allowEdit" | default "false" }}
{{ $moreControl := .Get "moreControl" | default "true" }}
{{ $searchControl := .Get "searchControl" | default "true" }}
{{ $tilelayersControl := .Get "tilelayersControl" | default "null" }}
{{ $embedControl := .Get "embedControl" | default "null" }}
{{ $datalayersControl := .Get "datalayersControl" | default "true" }}
{{ $onLoadPanel := .Get "onLoadPanel" | default "none" }}
{{ $captionBar := .Get "captionBar" | default "true" }}

{{ $scale := .Get "scale" }}
{{ $coordX := .Get "coordX" }}
{{ $coordY := .Get "coordY" }}

<iframe width="{{ $mapWidth }}" height="{{ $mapHeight }}" frameBorder="0" src="https://framacarte.org/fr/map/{{- $mapName -}}?scaleControl={{ $scaleControl }}&miniMap={{ $miniMap }}&scrollWheelZoom={{ $scrollWheelZoom }}&zoomControl={{ $zoomControl }}&allowEdit={{ $allowEdit }}&moreControl={{ $moreControl }}&searchControl={{ $searchControl }}&tilelayersControl={{ $tilelayersControl }}&embedControl={{ $embedControl }}&datalayersControl={{ $datalayersControl }}&onLoadPanel={{ $onLoadPanel }}&captionBar={{ $captionBar }}{{ with $scale}}#{{ . }}{{ end }}/{{ $coordX }}/{{ $coordY }}"></iframe>
{{< /highlight >}}

## Les paramètres
Tous est dans L'URL:

Exemple: *https://framacarte.org/fr/map/voyages-a-velo_153439#8/44.582/5.219* 

- zoom 8
- coordX 44.582
- coordY 5.219

Pour la suite:

 - coordX (default auto) **Voir dessus**
 - coordY (default auto) **Vois dessus**
 - scale (default auto) **Niveau de zoom, voir dessus**
 - scaleControl (default true) **Plein écran**
 - miniMap (default false)  **La minimap**
 - scrollWheelZoom (default true) **Zoom Souris**
 - zoomControl (default true)  **Barre du zoom**
 - allowEdit (default false) **Édition**
 -  moreControl (default true) **Bouton plus**
 - searchControl (default true) **Recherche**
 - tilelayersControl (default null) **Changer de fond de carte**
 - embedControl (default null) **Voir le partage**
 - datalayersControl (default true) **Voir les calques de données**
 - onLoadPanel (default none) **Barre de chargement**
 - captionBar (default true) **Barre des légendes**


## Exemple
L'URL d'une carte  https://framacarte.org/fr/map/voyages-a-velo_153439#10/45.2662/5.2322

Le nom c est *voyages-a-velo_153439* dans le code ça donne *mapName="voyages-a-velo_153439"

{{< highlight go-html-template >}}
{{</* frumap mapHeight="600" mapWidth="600" mapName="voyages-a-velo_153439" scale="8" coordX="44.582" coordY="5.219" */>}}
{{< /highlight >}}

{{< frumap mapHeight="600" mapWidth="600" mapName="voyages-a-velo_153439" scale="8" coordX="44.582" coordY="5.219" >}}

## Liens
https://framacarte.org/fr/

https://github.com/Hanzei/hugo-component-osm

https://stackoverflow.com/questions/68036749/embedding-iframe-in-hugo-site



