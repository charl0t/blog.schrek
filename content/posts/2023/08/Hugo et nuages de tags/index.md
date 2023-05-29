---
title: "Nuage de tags"
date: 2023-08-05
draft: false
tags: ["Tags","Hugo","Cloud"]
categories: ["Web"]
series: ["Hugo"]
image: "cloud.webp"
toc: true
---
Dans la barre des menus, j'avais trop de tags cela devenait pas trop lisible.

J'ai choisi de déporter les tags dans une page et d'utiliser que du CSS pour le visuel.

Il y a la possibilité de bibliothèques JavaScript mais je veux rester *light*.

## Les fichiers
On va créer la page qui va afficher le nuage. 

*/content/pages/tagscloud/index.md*

{{< highlight toml >}}
---
title: "Nuage de tags"
date: 2023-04-07T14:38:35+02:00
layout: tagscloud
toc: false
---
{{< /highlight >}}

- layout: tagscloud --> appel la page *tagscloud.html* du thème

On va la créer aussi:
 
*/themes/VOTRETHEME/layouts/_default/tagscloud.html*

{{< highlight go-html-template >}}
<!--tagscloud.html, /content/page/tagscloud/index.md -->
<!DOCTYPE html>
<html lang="fr">
    {{- partial "head.html" . -}}
    {{- partial "header.html" . -}}
    {{- partial "tagscloud.html" . -}}
    {{- partial "footer.html" . -}}
    {{- partial "scripts.html" . -}}
         </body>
</html>
{{< /highlight >}}

J'ai utilisé les *partials* pour avoir un code plus clair. 

Le code est adapté au CSS [Uikit](https://getuikit.com/).

{{< bandeau success >}}Vous pouvez facilement personnaliser le rendu, en changeant les valeurs du code. {{< / bandeau >}} 


*/themes/VOTRETHEME/layouts/partials/tagscloud.html*

{{< highlight go-html-template >}}
{{ if isset .Site.Taxonomies "tags" }}
	{{ if not (eq (len .Site.Taxonomies.tags) 0) }}
	<div class="uk-container uk-container-xsmall uk-background-muted uk-padding">
		<h1>Nuage de tags</h1>
			<ul class="uk-list uk-list-large">
				{{ range $name, $items := .Site.Taxonomies.tags }}
					{{ if and (ne $name "radio") (ne $name "about") (ne $name "")}}
						{{ $len := len $items }}
						{{ if lt $len 2 }}
							<li><a style="font-size: 18px" class="uk-text-success" href="{{ $.Site.BaseURL }}tags/{{ $name | urlize  }}"> {{ $name | title }} <span class="uk-text-emphasis" >({{ len $items }})</span></a></li>
						{{ else if le $len 3}}
							<li><a style="font-size: 16px" class="uk-text-primary" href="{{ $.Site.BaseURL }}tags/{{ $name | urlize  }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{ else if le $len 5}}
							<li><a style="font-size: 18px" class="uk-text-warning " href="{{ $.Site.BaseURL }}tags/{{ $name | urlize  }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{ else if le $len 7}}
							<li><a style="font-size: 24px" class="uk-text-danger" href="{{ $.Site.BaseURL }}tags/{{ $name | urlize }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{ else if le $len 9}}
							<li><a style="font-size: 21px" class="uk-text-warning " href="{{ $.Site.BaseURL }}tags/{{ $name | urlize }}"> {{ $name | title }} <span class="uk-text-emphasis" >({{ len $items }})</span></a></li>
						{{ else if le $len 11}}
							<li><a style="font-size: 22px" class="uk-text-primary" href="{{ $.Site.BaseURL }}tags/{{ $name | urlize  }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{ else if le $len 15}}
							<li><a style="font-size: 24px" class="uk-text-warning " href="{{ $.Site.BaseURL }}tags/{{ $name | urlize  }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{ else if le $len 30}}
							<li><a style="font-size: 30px" class="uk-text-danger" href="{{ $.Site.BaseURL }}tags/{{ $name | urlize  }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{ else if le $len 60}}
							<li><a style="font-size: 21px" class="uk-text-success" href="{{ $.Site.BaseURL }}tags/{{ $name | urlize  }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{ else if le $len 120}}
							<li><a style="font-size: 19px" class="uk-text-secondary" href="{{ $.Site.BaseURL }}tags/{{ $name | urlize }}"> {{ $name | title }} <span class="uk-text-emphasis">({{ len $items }})</span></a></li>
						{{end}}
					{{ end }}
				{{ end }}
			</ul>
	</div>
	{{ end }}
{{ end }}
{{< /highlight >}}

## Résultats

[Page nuage de tags]({{< ref "/pages/tagscloud.md" >}}  "Nuage")

## Liens

https://mertbakir.gitlab.io/hugo/tag-cloud-in-hugo/

https://blog.cubieserver.de/2020/adding-a-tag-cloud-to-my-hugo-blog/

https://discourse.gohugo.io/t/tag-cloud-for-hugo/43081/4

{{< chat cactus-comments >}}
