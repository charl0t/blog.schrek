---
title: "Shortcode Peertube"
date: 2023-07-05
draft: false
tags: ["Shortcode", "Peertube","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "peertube.webp"
toc: true
---
{{< figure src="brand.webp" title="" width=200px class="imagearticle" >}}






## Le code original

{{< highlight html >}}
<iframe title="Roch Sauquere - La Vérité Cachée de la conquete spatiale" src="https://www.peertube.fr/videos/embed/b9498316-89c5-45f6-b567-06aff8de799b" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups" width="560" height="315" frameborder="0"></iframe>
{{< /highlight >}}

Des idées sur l'iframe en mode Hugo [ici](https://stackoverflow.com/questions/68036749/embedding-iframe-in-hugo-site).

Sinon il y a les shortcodes.

## Le Shortcode
On va créer dans le dossier des shortcodes */themes/VOTRETHEME/layouts/shortcodes* un fichier pad.html
{{< highlight html >}}
{{ $PadName := .Get "PadName" }}
{{ $showControls := .Get "showControls" | default "false" }}
{{ $showChat := .Get "showChat" | default "false" }}
{{ $showLineNumbers := .Get "showLineNumbers" | default "true" }}
{{ $width := .Get "width" | default "100%" }}
{{ $height := .Get "height" | default "600" }}
{{ $height := .Get "height" | default "600" }}
{{ $useMonospaceFont := .Get "useMonospaceFont" | default "false" }}

<iframe name="embed_readwrite" src="https://hebdo.framapad.org/p/{{- $PadName -}}?showControls={{- $showControls -}}&showChat={{- $showChat -}}&showLineNumbers={{- $showLineNumbers -}}&useMonospaceFont=false" width="{{- $width -}}" height="{{- $height -}}" frameborder="0"></iframe>
{{< /highlight >}}

## Les paramètres



## Exemple



## Liens

https://joinpeertube.org/fr/


{{< chat cactus-comments >}}

