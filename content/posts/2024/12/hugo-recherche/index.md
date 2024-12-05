---
title: "Hugo et les recherches"
date: 2024-12-25
draft: false
tags: ["Markdown", "Html","Hugo","Pagefind"]
categories: ["Web"]
series: ["Hugo"]
image: "hugo.webp"
toc: true
---

Pour faciliter les recherches sur mon site, j'ai ajouté Pagefind

Pagefind est un outil de recherche rapide et efficace conçu pour les sites web statiques. Contrairement aux solutions classiques qui nécessitent un serveur ou une base de données, Pagefind indexe les contenus directement lors de la compilation du site et permet une recherche instantanée via JavaScript, sans dépendance serveur.

<!--more-->

## Caractéristiques principales

- Léger et rapide : Le fichier d’index est compressé et ne charge que les parties nécessaires, garantissant des performances élevées même sur des sites volumineux.
- Facilité d’intégration : Compatible avec de nombreux générateurs de sites statiques comme Hugo ou Jekyll. Il suffit d’ajouter l’outil lors du processus de build.
- Multilingue : Supporte plusieurs langues, rendant les recherches précises même dans des contextes linguistiques variés.
- Accessibilité : Les résultats sont rendus en HTML, assurant une compatibilité avec les lecteurs d’écran et autres outils d'accessibilité.

## Installation 
Bien documenté sur le site de Pagefind


{{< highlight bash  >}}
$ python3 -m pip install 'pagefind[extended]'
{{< /highlight >}}

## Indexation
On va demander a Pagefind d'indexer notre dossier public (celui que hugo fabrique).
Il faut se placer dans le dossier de notre site Hugo.

{{< highlight bash  >}}
$ python3 -m pagefind --site "public"
Running Pagefind v1.2.0 (Extended)
Running from: "/home/tuxien/projet/blog.schrek"
Source:       "public"
Output:       "public/pagefind"

[Walking source directory]
Found 491 files matching **/*.{html}

[Parsing files]
Did not find a data-pagefind-body element on the site.
↳ Indexing all <body> elements on the site.

[Reading languages]
Discovered 2 languages: unknown, fr
1 page found without an html lang attribute. 
Merging these pages with the fr language, as that is the main language on this site. 
Run Pagefind with --verbose for more information.

[Building search indexes]
Total: 
  Indexed 1 language
  Indexed 490 pages
  Indexed 7607 words
  Indexed 0 filters
  Indexed 0 sorts

Finished in 2.373 seconds


{{< /highlight >}}

Le script Pagefind va indexer notre site et créer un dossier **pagefind**, qui va nous servir pour la recherche.

## Page Recherche 

Pour mon site, j'ai décidé de faire une page dédiée a la recherche.

https://schrek.fr/pages/search/


{{< highlight yaml  >}}
---
title: "Recherche"
date: 2023-04-07T14:38:35+02:00
layout: search
toc: false
---


<!--Recherche-->
<script src="/pagefind/pagefind-ui.js" type="text/javascript"></script>
<script>
  window.addEventListener('DOMContentLoaded', (event) => {
    new PagefindUI({
      baseUrl: "/",
      // search element id
      element: "#search",
      // do not show images
      showImages: false,
      // I want to use my own CSS
      resetStyles: true,
      // do not show subresults of the same page
      showSubResults: false,
    excerptLength: 15,

    });
  });
</script>
<div class="uk-container-large">
	<div id="search" </div> 
</div>
   
{{< /highlight >}}


## Liens

https://pagefind.app/

https://gohugo.io/tools/search/

