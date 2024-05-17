---
title: "Shortcode pour integrer le HTML"
date: 2023-07-05
draft: false
tags: ["Shortcode", "Html","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "peertube.webp"
toc: true
---
{{< figure src="brand.webp" title="" width=200px class="imagearticle" >}}

On pourrait ecrire des milliers de shorcode pour integrer du html, mais il y a plus facile.

Pour l'exemple, on va prendre des videos diffusé sur [Peertube.fr](https://www.peertube.fr/)

## Le code original

{{< highlight html >}}
<iframe title="GoGoCarto - 1 - Personnalisation du site" src="https://www.peertube.fr/videos/embed/54509567-9116-4264-ba86-6c2d20cd360b" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups" width="560" height="315" frameborder="0"></iframe>
{{< /highlight >}}

Des idées sur l'iframe en mode Hugo [ici](https://stackoverflow.com/questions/68036749/embedding-iframe-in-hugo-site).

## Le Shortcode 
On va créer dans le dossier des shortcodes */themes/VOTRETHEME/layouts/shortcodes*, un fichier *rawhtml.html*.
Avec seulement ca.

{{< highlight html >}}
{{.Inner}}
{{< /highlight >}}


## Exemple
Il suffit de coller l'iframe entre nos 2 balises.

{{< highlight html >}}
{{</* rawhtml */>}}
<iframe title="GoGoCarto - 1 - Personnalisation du site" src="https://www.peertube.fr/videos/embed/54509567-9116-4264-ba86-6c2d20cd360b" allowfullscreen="true" sandbox="allow-same-origin allow-scripts allow-popups" width="560" height="315" frameborder="0"></iframe>
{{</* /rawhtml */>}}
{{< /highlight >}}

{{< rawhtml>}}
<iframe title="GoGoCarto - 1 - Personnalisation du site" src="https://www.peertube.fr/videos/embed/54509567-9116-4264-ba86-6c2d20cd360b" allowfullscreen="true" sandbox="allow-same-origin allow-scripts allow-popups" width="560" height="315" frameborder="0"></iframe>
{{< /rawhtml >}}

## Liens
https://www.peertube.fr/

https://joinpeertube.org/fr/



