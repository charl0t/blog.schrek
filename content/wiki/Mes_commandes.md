---
title: "Mes commandes"
date: 2023-04-07
categories: ["Wiki"]
layout: wiki
toc: true
---

## Creer un article 
*archetypes/post-bundle/post.md*
{{< highlight bash >}}
$ hugo new --kind post-bundle posts/2023/
{{< /highlight >}}

##  Compresser les png
{{< highlight bash >}}
$ find content/ -type f -iname '*.png' -exec  pngquant --force --quality=40-100 --skip-if-larger --strip --verbose {} --output {} \;
{{< /highlight >}}

## Convertir les jpg/png en wepb
{{< highlight bash >}}
$ cwebp -q 60 file.jpg -o file.wepb
{{< /highlight >}}

## Optimiser un jpg
{{< highlight bash >}}
$ jpegoptim  *.jpg
{{< /highlight >}}

## Voir les futurs articles en local
{{< highlight bash >}}
$ hugo serve -D -F
{{< /highlight >}}
 
## Voir le site en local
{{< highlight bash >}}
$ hugo serve --noHTTPCache --ignoreCache --buildDrafts
{{< /highlight >}}

## Compile le site 
{{< highlight bash >}}
$ hugo --minify
{{< /highlight >}}

## Compresse .js
{{< highlight bash >}}
$ uglifyjs fuse.min.js -o fuse.min.js
{{< /highlight >}}


