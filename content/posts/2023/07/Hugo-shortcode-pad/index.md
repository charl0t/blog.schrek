---
title: "Shortcode Framapad"
date: 2023-07-01
draft: false
tags: ["Shortcode", "Framapad","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "pad.wepb"
toc: true
---
{{< figure src="pad.wepb" title="" width=200px class="imagearticle" >}}

## Framapad

Un « pad » est un éditeur de texte collaboratif en ligne géré par [Framasoft](https://framapad.org/abc/fr/).


## Le code original

{{< highlight html >}}
<iframe name="embed_readwrite" src="https://hebdo.framapad.org/p/fygijewtbk-a0wa?showControls=true&showChat=true&showLineNumbers=true&useMonospaceFont=false" width="100%" height="600" frameborder="0"></iframe>
{{< /highlight >}}

On peut utiliser l'import de l'iframe.

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

{{< pad PadName="fygijewtbk-a0wa" showControls="false" showChat="false" useMonospaceFont="true" >}}

## Liens

https://framapad.org/abc/fr/


{{< chat cactus-comments >}}

