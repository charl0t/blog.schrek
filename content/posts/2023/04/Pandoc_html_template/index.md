---
title: "Pandoc html template"
date: 2023-04-20
draft: false
tags: ["Linux","Pandoc","Markdown"]
categories: ["Web"]
image: "icon_pandoc_square_small.webp"
toc: true
---
{{< figure src="icon_pandoc_square_small.webp" title="" width=200px class="imagearticle" >}}

Pour  gérer les templates avec Pandoc, on va utiliser un système de balises qui sont incluses dans l’entête du  fichier Markdown.
 
{{< highlight toml >}}
---
title: Schrek
subtitle: Mon jolie site
abstract: Test template
abstract-title: test abstract-title
author: Schrek christophe
date: 2023-03-23
site: https://schrek.fr/
subject: Pandoc template
description: utilisation des templates avec Pandoc
logo: logo.png
lang: fr
keywords: pandoc html5 css template
category: Web
---
{{< /highlight >}}


## Exemple de template
{{< highlight html >}}
<!DOCTYPE html>
<html> 
<head>
    <meta charset="utf-8">
    <html $if(lang)$ lang="$lang$" $endif$
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    $for(description)$<meta name="description" content="$description$">$endfor$
    <title>$if(title)$$title$$endif$</title>
    $for(keywords)$<meta name="keywords" content="$keywords$">$endfor$
    $for(author)$<meta name="author" content="$author$"/>$endfor$
    $if(date)$<meta name="date" content="$date$"/>$endif$
    <link rel="stylesheet" href="styles.css">
</head>
<header>
    $if(title)$<h1>$title$</h1>$endif$
    $if(date)$<h3>$date$</h3>$endif$
    $if(author)$<p>$author$</p>$endif$
</header>
<main>
    $if(subject)$<h3>$subject$</h3>$endif$
    $if(description)$<p>$description$</p>$endif$
    $if(category)$<p>$category$</p>$endif$
<nav>
$if(toc)$
$toc$
$endif$
</nav>

<article>
$body$
</article>
</main>
</html>
{{< /highlight >}}

## Compilation du document html
J’ai fait un petit exemple avec plein de balises Markdown. On peut remarquer que les cases à cocher ça marche pas.

[test.md.txt *(clic droit enregistrer sous)*](test.md.txt)

{{< highlight bash >}}
pandoc -s -f markdown+smart  --template template.html --toc --metadata  --to=html5 test.md -o index.html
{{< /highlight >}}

Ça donne un fichier HTML brut. 



[index.html *(clic droit enregistrer sous)*](index.html)

Il reste l’habillage avec du CSS (vite fait avec bootstrap), il faut recompiler le fichier a chaque modification du template.



[index-2.html *(clic droit enregistrer sous)*](index-2.html)


## Liens
https://pandoc.org/MANUAL.html#using-variables-in-templates

https://github.com/ryangrose/easy-pandoc-templates

https://maehr.github.io/academic-pandoc-template/




