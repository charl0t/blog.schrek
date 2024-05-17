---
title: "Shortcode les fichiers"
date: 2023-07-15
draft: false
tags: ["Shortcode","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "paper.webp"
toc: true
---
{{< figure src="paper.webp" title="" width=200px class="imagearticle" >}}
Ce shortcode liste les fichiers dans une dossier pour permettre leurs téléchargements.

Dans le dossier de l'article, il faut creer un dossier *files/* pour y deposer les fichiers.

{{< bandeau warning >}} Attention, le shortcode ne marche pas si il y a des espaces dans le nom du dossier de l'article {{< / bandeau >}} 

<--more-->

## Le shortcode

On va créer dans le dossier des shortcodes */themes/VOTRETHEME/layouts/shortcodes* un fichier pj.html

### pj.html
{{< highlight go-html-template >}}
{{ $_hugo_config := `{ "version": 1 }` -}}
<div class="attachments-files uk-card uk-card-small uk-width-1-3@m uk-padding">
  <h3 class="attachments-files-titre">Téléchargement  <span uk-icon="icon: cloud-download;ratio:2"></span></h3> 
  <div class="attachments-files">
  {{- $filesName := "files" }}
  {{- if ne .Page.File.BaseFileName "index" }}
    {{- $filesName = printf "%s.files" .Page.File.BaseFileName }}
  {{- end}}
  {{- $fileDir := replace .Page.File.Dir "\\" "/" }}
  {{- $pattern := .Get "pattern" | default "" }}
  {{- range (readDir (printf "content/%s%s" .Page.File.Dir $filesName) ) }}
    <li>
      <a href="{{ (printf "%s%s/%s" $fileDir $filesName .Name) | relLangURL }}">{{.Name}}</a>
    </li>
  {{- end}}
  </div>
  {{- .Inner}}
</div>
{{< /highlight >}}

### le CSS pour uikit

{{< highlight css >}}
.attachments-files{
background-color: #dbe6eb;
}
{{< /highlight >}}

## Résultat

{{< highlight go-html-template >}}
{{</* pj /*/>}}
{{< /highlight >}}

{{< pj />}}

## Liens
http://oostens.me/posts/hugo-attachment-shortcode/

https://fr.wikisource.org/wiki/%C3%89mile_Zola_(Maupassant)


