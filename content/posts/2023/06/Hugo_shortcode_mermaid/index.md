---
title: "Shortcode Mermaid"
date: 2023-06-05
draft: false
tags: ["Shortcode", "Mermaid","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "mermaid.webp"
toc: true
---
{{< figure src="mermaid.webp" title="" width=200px class="imagearticle" >}}

On va integrer [mermaid](https://mermaid.js.org/) dans Hugo.

Mermaid permet de générer des jolies diagrammes  à partir de texte.

[Kroki](https://kroki.io/) est une alternative.

## Le code
On va creer dans notre dossier des shortcodes */themes/VOTRETHEME/layouts/shortcodes* un fichier mermaid.html

{{< highlight html >}}
<div class="mermaid">
    {{ .Inner | safeHTML }}
</div>
{{ if le (.Page.Scratch.Get "mermaidInserted") 0 }}
{{ .Page.Scratch.Add "mermaidInserted" 1 }}
{{ $mermaid := resources.Get "js/mermaid.min.js" | minify | fingerprint }}
<script type="application/javascript" src="{{ $mermaid.Permalink }}" defer></script>
<script type="module">
    mermaid.initialize({});
</script>
{{ end }}
{{< /highlight >}}

## mermaid.min.js

On recupere le fichier *mermaid.min.js* pour le placer dans le dossier */themes/VOTRETHEME/assets/js*

{{< highlight bash >}}
$ wget https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js
{{< /highlight >}}

## Le Shortcode

{{< highlight go-html-template >}}
{{</* mermaid */>}}
sequenceDiagram
    Louise->>Robert: Salut
    Robert-->>Louis: Bien!
    Louis-)Robert: A plus tard!
{{</* / mermaid */>}}
{{< /highlight >}}

## Tests

vous pouvez tester vos code [ici](https://mermaid.live)

## Exemples

{{< mermaid >}}
sequenceDiagram
    Louise->>Robert: Salut
    Robert-->>Louis: Bien!
    Louis-)Robert: A plus tard!
{{</ mermaid >}}


{{< mermaid >}}
pie title Hugo c'est cool?
    "Oui" : 25
    "Oui en jaune" : 75
{{< / mermaid >}}

## Liens

https://satoru.dev/2020/08/using-mermaid-in-hugo/

https://robb.sh/posts/how-to-use-mermaid-diagrams-in-hugo/

https://mermaid.js.org/intro/

{{< chat cactus-comments >}}

