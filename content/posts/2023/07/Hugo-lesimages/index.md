---
title: "Hugo et les images"
date: 2023-07-20
draft: false
tags: ["Shortcode","Hugo","Images"]
categories: ["Web"]
series: ["Hugo"]
image: "image.webp"
toc: true
---

## Minimal
{{< highlight go-html-template >}}
{{</* figure src="image.webp" width=200px */>}}
{{< /highlight >}}

{{< figure src="image.webp" width=200px >}}

## Grande taille
{{< highlight go-html-template >}}
{{/*< figure src="image.webp" title="Anita Austvika" caption="Photo de [Anita Austvika](https://unsplash.com/ko/@anitaaustvika) sur [Unsplash](https://unsplash.com/)"  width=800px alt="Anita Austvika" class="imagecenter" attrlink="https://unsplash.com/fr/photos/u9ZFCP8VuvU"*/>}}
{{< /highlight >}}
{{< figure src="image.webp" title="Anita Austvika" caption="Photo de [Anita Austvika](https://unsplash.com/ko/@anitaaustvika) sur [Unsplash](https://unsplash.com/)"  width=800px alt="Anita Austvika" class="imagecenter" attrlink="https://unsplash.com/fr/photos/u9ZFCP8VuvU">}}

## Images centrée
{{< highlight go-html-template >}}
{{</* figure src="image.webp" title="Anita Austvika" caption="Photo de [Anita Austvika](https://unsplash.com/ko/@anitaaustvika) sur [Unsplash](https://unsplash.com/)"  width=400px alt="Anita Austvika" class="imagecenter" */>}}
{{< /highlight >}}
{{< figure src="image.webp" title="Anita Austvika" caption="Photo de [Anita Austvika](https://unsplash.com/ko/@anitaaustvika) sur [Unsplash](https://unsplash.com/)"  width=400px alt="Anita Austvika" class="imagecenter">}}

## Images à droite
{{< figure src="image.webp" title="Anita Austvika" caption="Photo de [Anita Austvika](https://unsplash.com/ko/@anitaaustvika) sur [Unsplash](https://unsplash.com/)"  width=300px alt="Anita Austvika" class="imageright">}}"
{{< highlight go-html-template >}}
{{</* figure src="image.webp" title="Anita Austvika" caption="Photo de [Anita Austvika](https://unsplash.com/ko/@anitaaustvika) sur [Unsplash](https://unsplash.com/)"  width=400px alt="Anita Austvika" class="imageright" */>}}
{{< /highlight >}}




## Le CSS
{{< highlight css >}}
.imagecenter {
    display: grid;
    align-items: center;
    justify-content: center;
    text-align: center;
}
.imageright {
    display: grid;
    align-items: right;
    justify-content: right;
    text-align: center;
}
.imageleft {
    display: grid;
    align-items: left;
    justify-content: left;
    text-align: center;
}
{{< /highlight >}}

## lien

https://gohugo.io/content-management/shortcodes/#use-hugos-built-in-shortcodes
