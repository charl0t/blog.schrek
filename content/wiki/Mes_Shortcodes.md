---
title: "Mes Shortcodes"
date: 2023-04-07
categories: ["Wiki"]
tags : ["shortcode"]
layout: wiki
toc: true
---
## Images

{{< highlight go-html-template >}}
{{</* figure src="codepen-logo-8.png" title="" width=200px class="imagearticle" */>}}
{{< /highlight >}}


## Icones

https://getuikit.com/docs/icon

{{< highlight go-html-template >}}
{{</* uicon heart 2 */>}} est un **gros** coeur.
{{< /highlight >}}

{{< uicon heart 2 >}} est un **gros** coeur.

## Bandeaux

{{< highlight go-html-template >}}

{{</* bandeau primary */>}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{</* / bandeau */>}} 

{{</* bandeau success */>}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{</* / bandeau */>}} 

{{</* bandeau warning */>}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{</* / bandeau */>}} 

{{</* bandeau danger */>}} Lorem **ipsum** dolor sit amet, *consectetur* adipiscing elit, sed do eiusmod tempor incididunt. {{</* / bandeau */>}} 
{{< /highlight >}}

## Codepen
https://codepen.io

{{< highlight go-html-template >}}
{{</* codepen YzObPmg */>}}  
{{< /highlight >}}


## MermaidJs
https://mermaid.js.org/

{{< highlight go-html-template >}}
{{</* mermaid */>}}
sequenceDiagram
    Louise->>Robert: Salut
    Robert-->>Louis: Bien!
    Louis-)Robert: A plus tard!
{{</* / mermaid */>}}
{{< /highlight >}}

## ChartJS
https://www.chartjs.org/

{{< highlight go-html-template >}}
{{</* chart /*>}}
{
  type: 'radar',
  data: {},
  options: {}

}
{{</* /chart */>}}
{{< /highlight >}}

## Chat
https://cactus.chat/docs/integrations/hugo/

{{< highlight go-html-template >}}
{{</* chat cactus-comments */>}}
{{< /highlight >}}

## Documents
Creer un dossier *files* dans le dossier de l'article. 

*Sans le /* apres {{*

{{< highlight go-html-template >}}
{{/*% pj /%}}
{{< /highlight >}}

## Badges
https://getuikit.com/docs/icon

https://getuikit.com/docs/label#style-modifiers

{{< chat cactus-comments >}}
{{< highlight go-html-template >}}
{{</* badge pencil warning */>}}
**Mise a jour**
{{</* /badge */>}}
{{< /highlight >}}

## Galeries
- creer un dossier *image/*
- titre -> Nom de la galerie
- animation -> Type de transition *slide,fade,scale* (des exemples sur [Uikit](https://getuikit.com/docs/lightbox#animations))

{{< highlight go-html-template >}}
{{</* galerie titre="super galerie" animation="scale" */>}}
{{< /highlight >}}
