---
title: "Hugo et les galeries"
date: 2023-07-25
draft: false
tags: ["Shortcode","Hugo","Images","Galerie"]
categories: ["Web"]
series: ["Hugo"]
image: "gallery.webp"
toc: true
---
Une petite galerie toute simple, qui utilise Uikit et lightbox.

Dans le dossier de l'article, il faut créer un dossier *images/* pour y deposer les images.

Hugo va directement chercher les images.


{{< galerie >}}

## Shortcode
{{< highlight go-html-template >}}
<!--
Options:
    titre -> Nom de la galerie
    animation -> Type de transition slide,fade,scale (des exemples sur Uikit:https://getuikit.com/docs/lightbox#animations)
Exemples:
galerie titre="super galerie" animation="scale"
-->

{{ $titre := .Get "titre"| default "Galerie" }}
{{ $animation := .Get "animation" | default "fade"}}
{{ $image :=  .Page.Resources.Match "images/*" }}

<div class="uk-h3">{{ $titre }}</div>
<div class="uk-child-width-1-3@m" uk-grid uk-lightbox="animation: {{ $animation }}">
{{ with $image }}
    {{ range . }}
    {{ $resized := .Resize "300x webp" }}
    <div>
        <a class="uk-inline" href="{{ .Permalink }}" data-caption="{{ path.Base .Name }}">
            <img src="{{ $resized.Permalink }}" width="1800" height="1200" alt="">
        </a>
    </div>
    {{ end }}
{{ end }}
</div>
{{< /highlight >}}

## Options

- titre -> Nom de la galerie
- animation -> Type de transition *slide,fade,scale* (des exemples sur [Uikit](https://getuikit.com/docs/lightbox#animations))

{{< highlight go-html-template >}}
{{</* galerie titre="super galerie" animation="scale" */>}}
{{< /highlight >}}

{{< galerie titre="super galerie" animation="scale" >}}

## Liens
https://getuikit.com/docs/lightbox#animations

https://unsplash.com/pt-br/@neom

{{< chat cactus-comments >}}

