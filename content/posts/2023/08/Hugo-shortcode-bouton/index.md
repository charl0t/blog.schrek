---
title: "Shortcode bouton"
date: 2023-08-12
draft: false
tags: ["Shortcode", "Bouton","Uikit"]
categories: ["Web"]
series: ["Hugo"]
image: "lien.webp"
toc: true
---

J'avais besoin d"un bouton pour ouvrir des liens.


## Le shortcode
A déposer dans */themes/VOTRETHEME/layouts/shortcodes/bouton.html*.

On peut personaliser l'icône grace a [Uikit](https://getuikit.com/docs/icon)

{{< highlight go-html-template >}}
{{ $url := .Get "url" }}
{{ $titre := .Get "titre" }}
{{ $icone := .Get "icone" | default "link"}}

<a class="uk-button uk-button-default uk-box-shadow-medium" target="_blank" href="{{ $url }}"><span uk-icon="icon: {{ $icone }}"></span> {{ $titre }}</a>
{{< /highlight >}}

## Exemples

{{< highlight go-html-template >}}
{{</* bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/dgnpzyngzbqk" icone="forward" */>}}
{{< /highlight >}}


{{< bouton titre="Voir sur overleaf" url="https://www.overleaf.com/read/dgnpzyngzbqk" icone="forward" >}}


{{< highlight go-html-template >}}
{{</* bouton titre="Uikit" url="https://getuikit.com" icone="uikit" */>}}
{{< /highlight >}}

{{< bouton titre="Uikit" url="https://getuikit.com" icone="uikit" >}}

## Liens

https://getuikit.com/docs/button

https://getuikit.com/docs/icon



{{< chat cactus-comments >}}

