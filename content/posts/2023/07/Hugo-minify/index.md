---
title: "Hugo minification"
date: 2023-07-20
draft: false
tags: ["Shortcode","Hugo","Minify"]
categories: ["Web"]
series: ["Hugo"]
image: "minifycss.webp"
toc: true
---
Hugo est rapide, mais on peut améliorer le chargement des ressources.

## Les images
Il faut utiliser des formats modernes comme [webp](https://fr.wikipedia.org/wiki/WebP) et avoir un bon redimensionnement.
J'utilise [Gimps](https://www.gimp.org/) pour changer la taille et le format.

Sinon en ligne de commande: 

{{< highlight bash >}}
$ cwebp -q 90 minifycss.png -o minifycss.webp
{{< /highlight >}}

## Les CSS
Les fichiers CSS sont placés directement dans */themes/VOTRETHEME/assets/css*.

Dans mon *partials/head.html*, j ai:

{{< highlight go-html-template >}}
{{ $css := resources.Get "css/uikit.min.css" | minify | resources.Fingerprint "sha512" }}
<link  href="{{ $css.RelPermalink }}" rel="stylesheet"  integrity="{{ $css.Data.Integrity }}" crossorigin="anonymous">
{{ $css := resources.Get "css/styles.css" | minify | resources.Fingerprint "sha512" }}
<link  href="{{ $css.RelPermalink }}" rel="stylesheet"  integrity="{{ $css.Data.Integrity }}" crossorigin="anonymous">
{{< /highlight >}}

Récupère le fichier CSS, compresse(minify) et créer une empreinte pour vérifier les changements (ca évite de recharger dans le cache si c'est le même fichier)

{{< highlight go-html-template >}}
{{ $css := resources.Get "css/uikit.min.css" | minify | resources.Fingerprint "sha512" }}
{{< /highlight >}}
Hugo remplace les valeurs dans le <link>
{{< highlight go-html-template >}}
<link  href="{{ $css.RelPermalink }}" rel="stylesheet"  integrity="{{ $css.Data.Integrity }}" crossorigin="anonymous">
{{< /highlight >}}

## Les JS
Les fichiers JS sont placés directement dans */themes/VOTRETHEME/assets/js*.

Dans mon *partials/head.html*, j'ai:

{{< highlight go-html-template >}}
{{ $js := resources.Get "js/uikit.min.js" | minify | resources.Fingerprint "sha512"}}
    <script src="{{ $js.RelPermalink }}" integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous"></script>
{{ $js := resources.Get "js/uikit-icons.min.js" | minify }}
    <script defer src="{{ $js.RelPermalink }}" integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous"></script>
{{ $js := resources.Get "js/jquery.min.js" | minify | resources.Fingerprint "sha512" }}
    <script defer src="{{ $js.RelPermalink }}" integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous"></script>
{{ $js := resources.Get "js/fuse.min.js" | minify | resources.Fingerprint "sha512" }}
    <script defer src="{{ $js.RelPermalink }}" integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous"></script>
{{ $js := resources.Get "js/mark.min.js" | minify | resources.Fingerprint "sha512" }}
    <script defer src="{{ $js.RelPermalink }}" integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous"></script>
{{ $js := resources.Get "js/jquery.mark.min.js" | minify | resources.Fingerprint "sha512" }}
    <script defer src="{{ $js.RelPermalink }}" integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous"></script>
{{ $js := resources.Get "js/search.js" | minify | resources.Fingerprint "sha512" }}
    <script defer src="{{ $js.RelPermalink }}" integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous"></script>
{{< /highlight >}}

Le principe est le même que pour le CSS.

## La commande
Pour finir, on va lancer cette commande pour créer le site.
{{< highlight bash >}}
$ hugo --minify
{{< /highlight >}}

J'ai testé le site sur [https://pagespeed.web.dev/](https://pagespeed.web.dev/).
{{< figure src="bureau.webp" width=300px >}}
{{< figure src="mobile.webp" width=300px >}}

J'ai encore des améliorations à faire au niveau du [cache](https://pagespeed.web.dev/analysis/https-schrek-fr/3o81b3lct9?hl=fr&form_factor=desktop) (dans le rapport: *Diffusez des éléments statiques grâce à des règles de cache efficaces*), mais ça avance.


## Liens
https://gohugo.io/hugo-pipes/minification/

https://digitaldrummerj.me/hugo-asset-pipeline/

https://makewithhugo.com/minify-and-load-css-through-hugo/

{{< chat cactus-comments >}}
