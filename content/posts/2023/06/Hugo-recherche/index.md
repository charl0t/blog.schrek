---
title: "Recherche dans Hugo"
date: 2023-06-01
draft: true
tags: ["Shortcode", "Recherche","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "search.webp"
toc: true
---
Il me manquait la recherche sur Hugo, *j'en est chié* une histoire de Jquery. 

## config.toml

On va demander a Hugo de générer un fichier JSON, pour récupérer les données du site.

{{< highlight toml>}}
[outputs]
    home = [ "HTML", "JSON", "RSS"]
{{< /highlight >}}

Quand on lance Hugo, on a droit a une erreur.

{{< highlight bash>}}
Change of config file detected, rebuilding site.
2023-05-02 11:39:09.348 +0200
WARN 2023/05/02 11:39:09 found no layout file for "JSON" for kind "home": You should create a template file which matches Hugo Layouts Lookup Rules for this combination.
Rebuilt in 205 ms
{{< /highlight >}}

## Index.json

il faut créer le fichier *index.json* dans notre theme *themes/schrek/layouts*

{{< highlight html>}}
{{- $.Scratch.Add "index" slice -}}
{{- range .Site.RegularPages -}}
    {{- $.Scratch.Add "index" (dict "title" .Title "tags" .Params.tags "categories" .Params.categories "contents" .Plain "permalink" .Permalink) -}}
{{- end -}}
{{- $.Scratch.Get "index" | jsonify -}}
{{< /highlight >}}

## Fichiers JS
- jquery.min.js
- fuse.min.js
- mark.min.js
- jquery.mark.min
- search.js

On peux choisir de charger  le footer:
 
{{< highlight html>}}
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js" integrity="sha512-pumBsjNRGGqkPzKHndZMaAG+bir374sORyzM3uulLV14lN5LyykqNk8eEeUlUkB3U0M4FApyaHraT65ihJhDpQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/fuse.js/6.6.2/fuse.min.js" integrity="sha512-Nqw1tH3mpavka9cQCc5zWWEZNfIPdOYyQFjlV1NvflEtQ0/XI6ZQ+H/D3YgJdqSUJlMLAPRj/oXlaHCFbFCjoQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mark.js/8.11.1/mark.min.js" integrity="sha512-5CYOlHXGh6QpOFA/TeTylKLWfB3ftPsde7AnmhuitiTX4K5SqCLBeKro6sPS8ilsz1Q4NRx3v8Ko2IBiszzdww==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mark.js/8.11.1/jquery.mark.js" integrity="sha512-19TrqSGVSwaC2IDGHrD+tAkX59/w5cXy0BHDVwn7OJQXxavORhFSFM7DOO9soXKuo8O7gGNHiG9R2vFrXRBcTQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script defer src="/js/search.js"></script>
{{< /highlight >}}


Sinon on les télécharge dans le dossier du thème  *themes/schrek/assets/js*
{{< highlight html>}}
{{ $js := resources.Get "js/jquery.min.js" | minify }}
{{< /highlight >}}

ca sert a réduire la taille du fichier pour un meilleur chargement.

{{< highlight html>}}
  <script defer src="{{ $js.RelPermalink }}"></script>
{{ $js := resources.Get "js/jquery.min.js" | minify }}
    <script defer src="{{ $js.RelPermalink }}"></script>
{{ $js := resources.Get "js/fuse.min.js" | minify }}
    <script defer src="{{ $js.RelPermalink }}"></script>
{{ $js := resources.Get "js/mark.min.js" | minify }}
    <script defer src="{{ $js.RelPermalink }}"></script>
{{ $js := resources.Get "js/jquery.mark.min.js" | minify }}
    <script defer src="{{ $js.RelPermalink }}"></script>
{{ $js := resources.Get "js/search.js" | minify }}
    <script defer src="{{ $js.RelPermalink }}"></script>
{{< /highlight >}}


## Search.js
On va creer le fichier *search.js* dans /static/js ou bien /asset/js selon ce que vous avez choisi.
{{< highlight js >}}
summaryInclude = 60;
var fuseOptions = {
    shouldSort: true,
    includeMatches: true,
    threshold: 0,
    tokenize: true,
    location: 0,
    distance: 100,
    maxPatternLength: 32,
    minMatchCharLength: 1,
    keys: [
        { name: "title", weight: 0.8 },
        { name: "contents", weight: 0.5 },
        { name: "tags", weight: 0.3 },
        { name: "categories", weight: 0.3 },
    ],
};
var searchQuery = param("s");
if (searchQuery) {
    $("#search-query").val(searchQuery);
    executeSearch(searchQuery);
} else {
    $("#search-results").append("<p>Un mot ou une phrase</p>");
}
function executeSearch(searchQuery) {
    $.getJSON("/index.json", function (data) {
        var pages = data;
        var fuse = new Fuse(pages, fuseOptions);
        var result = fuse.search(searchQuery);
        console.log({ matches: result });
        if (result.length > 0) {
            populateResults(result);
        } else {
            $("#search-results").append("<h1>Rien Trouvé</h1>");
        }
    });
}
function populateResults(result) {
    $.each(result, function (key, value) {
        var contents = value.item.contents;
        var snippet = "";
        var snippetHighlights = [];
        var tags = [];
        if (fuseOptions.tokenize) {
            snippetHighlights.push(searchQuery);
        } else {
            $.each(value.matches, function (matchKey, mvalue) {
                if (mvalue.key == "tags" || mvalue.key == "categories") {
                    snippetHighlights.push(mvalue.value);
                } else if (mvalue.key == "contents") {
                    start = mvalue.indices[0][0] - summaryInclude > 0 ? mvalue.indices[0][0] - summaryInclude : 0;
                    end = mvalue.indices[0][1] + summaryInclude < contents.length ? mvalue.indices[0][1] + summaryInclude : contents.length;
                    snippet += contents.substring(start, end);
                    snippetHighlights.push(mvalue.value.substring(mvalue.indices[0][0], mvalue.indices[0][1] - mvalue.indices[0][0] + 1));
                }
            });
        }
        if (snippet.length < 1) {
            snippet += contents.substring(0, summaryInclude * 2);
        }
        var templateDefinition = $("#search-result-template").html();
        var output = render(templateDefinition, { key: key, title: value.item.title, link: value.item.permalink, tags: value.item.tags, categories: value.item.categories, snippet: snippet });
        $("#search-results").append(output);
        $.each(snippetHighlights, function (snipkey, snipvalue) {
            $("#summary-" + key).mark(snipvalue);
        });
    });
}
function param(name) {
    return decodeURIComponent((location.search.split(name + "=")[1] || "").split("&")[0]).replace(/\+/g, " ");
}
function render(templateString, data) {
    var conditionalMatches, conditionalPattern, copy;
    conditionalPattern = /\$\{\s*isset ([a-zA-Z]*) \s*\}(.*)\$\{\s*end\s*}/g;
    copy = templateString;
    while ((conditionalMatches = conditionalPattern.exec(templateString)) !== null) {
        if (data[conditionalMatches[1]]) {
            copy = copy.replace(conditionalMatches[0], conditionalMatches[2]);
        } else {
            copy = copy.replace(conditionalMatches[0], "");
        }
    }
    templateString = copy;
    var key, find, re;
    for (key in data) {
        find = "\\$\\{\\s*" + key + "\\s*\\}";
        re = new RegExp(find, "g");
        templateString = templateString.replace(re, data[key]);
    }
    return templateString;
}
{{< /highlight >}}

## Search.html
Toujours dans notre thème dans le dossier */layouts/_default/* , ca sera la page de recherche, j'utilise uikit comme framework.

{{< highlight html>}}
{{ define "main" }}
<div class="uk-container uk-background-muted  uk-box-shadow-large uk-padding">
<div class="uk-margin">
  <form class="uk-search uk-search-default" action="{{ "search" | absURL }}">
      <span uk-search-icon></span>
      <input class="uk-search-input" type="search" placeholder="Search" aria-label="Search" id="search-query" name="s">
  </form>
  <div id="search-results">
    <h3>Résultats</h3>
   </div>
</div>
<!-- this template is sucked in by search.js and appended to the search-results div above. So editing here will adjust style -->
<script id="search-result-template" type="text/x-js-template">
  <article class="uk-article">
    <h3 class="uk-article-title"><a  href="${link}">${title}</a></a></h3>
    <p class="uk-article-meta">${ isset categories }<p>Categories: ${categories}</p>${ end }
    ${ isset tags }<p>Tags: ${tags}</p>${ end }</p>
    <p class="uk-text-lead">${snippet}</p>
  </article>
</script>
</div>
{{ end }}
{{< /highlight >}}

## Search.md
On revient a la racine du site dans le dossier *content/*, il faut créer un fichier search.md

{{< highlight markdown >}}

---
title: "Search Results"
sitemap:
  priority : 0.1
layout: "search"
---


This file exists solely to respond to /search URL with the related `search` layout template.

No content shown here is rendered, all content is based in the template layouts/page/search.html

Setting a very low sitemap priority will tell search engines this is not important content.

This implementation uses Fusejs, jquery and mark.js


## Initial setup

Search  depends on additional output content type of JSON in config.toml
\```
[outputs]
  home = ["HTML", "JSON"]
\```

## Searching additional fileds

To search additional fields defined in front matter, you must add it in 2 places.

### Edit layouts/_default/index.JSON
This exposes the values in /index.json
i.e. add `category`
\```
...
  "contents":{{ .Content | plainify | jsonify }}
  {{ if .Params.tags }},
  "tags":{{ .Params.tags | jsonify }}{{end}},
  "categories" : {{ .Params.categories | jsonify }},
...
\```

### Edit fuse.js options to Search
`static/js/search.js`
\```
keys: [
  "title",
  "contents",
  "tags",
  "categories"
]
\```
{{< /highlight >}}

## Presque fini

On lance hugo

{{< highlight bash >}}
$ hugo serve -D -F
{{< /highlight >}}

On a deja ca: 

http://localhost:1313/search/

## Barre de recherche
Pour la barre de recherche dans une menu .

{{< highlight html >}}
    <div class="uk-margin">
      <form class="uk-search uk-search-default" action='{{ with .GetPage "/search" }}{{.Permalink}}{{end}}' method="get" >
          <span uk-search-icon></span>
          <input class="uk-search-input" type="search" placeholder="Search" aria-label="Search" id="search-query" name="s">
      </form>
    </div>
{{< /highlight >}}

## Liens

https://schrek.fr/search/

https://javifm.com/en/blog/search-in-hugo-with-lunr/

{{< chat cactus-comments >}}
