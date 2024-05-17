---
title: "Mathématique dans Hugo"
date: 2024-02-10
draft: false
tags: ["Hugo", "Katex","Latex","Mathjax"]
categories: ["Hugo"]
series: ["Hugo"]
Image: "katex.webp"
toc: true
---

Dans la version [v0.122.0](https://github.com/gohugoio/hugo/releases/tag/v0.122.0), on peut facilement ajouter le support des formules mathématiques façon *LaTex*. Ce tutoriel est juste une retranscription de cette [page](https://gohugo.io/content-management/mathematics/).

$$E=mc^2$$

<!--more-->

## Installation:

Modification du ficher de configuration du blog.

*config.toml*
{{< highlight toml  >}}
[markup]
  [markup.goldmark]
    [markup.goldmark.extensions]
      [markup.goldmark.extensions.passthrough]
        enable = true
        [markup.goldmark.extensions.passthrough.delimiters]
          block = [['\[', '\]'], ['$$', '$$']]
          inline = [['\(', '\)']]
[params]
  math = true
{{< /highlight >}}

Ajout de d'une page partial 

*layouts/partials/math.html*
{{< highlight html  >}}
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<script>
  MathJax = {
    tex: {
      displayMath: [['\\[', '\\]'], ['$$', '$$']],  // block
      inlineMath: [['\\(', '\\)']]                  // inline
    }
  };
</script>
{{< /highlight >}}

On active le *partial* si math est activé dans config.

*layouts/_default/baseof.html*

{{< highlight html  >}}
...
  {{ if .Param "math" }}
    {{ partialCached "math.html" . }}
  {{ end }}
...
{{< /highlight >}}

## Utilisation simple

{{< highlight html  >}}
$$ a^*=x-b^* $$
{{< /highlight >}}


$$ a^*=x-b^* $$

{{< highlight html  >}}
$$ \frac{1}{2}$, $\left(-\frac{1}{2}\right)^n $$
{{< /highlight >}}

$$ \frac{1}{2}\left(-\frac{1}{2}\right)^n $$

## Utilisation complexe

{{< highlight html  >}}
$$\begin{align}
{V} & = \int_{-r}^{r} \pi(r^2-h^2) \mathrm{d}h \\[2ex]
& = \left[ \pi(hr^2-\tfrac{1}{3}h^3) \right]_{-r}^{r} \\[2ex]
& = \pi \left(r^3-\tfrac{1}{3}r^3 \right) - \pi \left(-r^3-\tfrac{1}{3}r^3 \right) \\[2ex]
& = \tfrac{2}{3} \pi r^3 + \tfrac{2}{3} \pi r^3 \\[2ex]
{V} & = \tfrac{4}{3} \pi r^3
\end{align}$$
{{< /highlight >}}

$$\begin{align}
{V} & = \int_{-r}^{r} \pi(r^2-h^2) \mathrm{d}h \\[2ex]
& = \left[ \pi(hr^2-\tfrac{1}{3}h^3) \right]_{-r}^{r} \\[2ex]
& = \pi \left(r^3-\tfrac{1}{3}r^3 \right) - \pi \left(-r^3-\tfrac{1}{3}r^3 \right) \\[2ex]
& = \tfrac{2}{3} \pi r^3 + \tfrac{2}{3} \pi r^3 \\[2ex]
{V} & = \tfrac{4}{3} \pi r^3
\end{align}$$

## Liens

https://github.com/gohugoio/hugo/releases/tag/v0.122.0

https://gohugo.io/content-management/mathematics/

https://www.mathjax.org/

https://jojozhuang.github.io/tutorial/mathjax-cheat-sheet-for-mathematical-notation/

https://www.mathematex.fr/guide-mathjax

https://www.sqlpac.com/fr/documents/mathjax-tex-guide-pratique-aide-memoire.html

https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm


