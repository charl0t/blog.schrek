---
title: "Commentaires dans Hugo"
date: 2024-03-05
draft: false
tags: ["Hugo", "Commentaires","Disqus"]
categories: ["Hugo"]
series: ["Hugo"]
Image: "disqus.webp"
toc: true
---
Le systeme de commentaires [Cactus](https://cactus.chat/docs/integrations/hugo/) ne me satisfait plus, j'ai décidé de tester [Disqus](https://disqus.com/).

<!--more-->

## Installation
Il suffit de suivre le tutoriel sur le site d'[Hugo](https://gohugo.io/content-management/comments/)

Rien de bien compliqué, c est un shortcode interne a Hugo.

Il faut deja creer un compte sur le site de [Disqus](https://disqus.com/profile/signup/).

On va récupérer le shortname dans la partie admin de [Disqus](https://schrek-fr.disqus.com/admin/settings/general/)

Dans notre fichier de configuration du site config.toml, on ajoute Disqus.

{{< highlight yalm  >}}

[services]
  [services.disqus]
    shortname = 'schrek-fr'

{{< /highlight >}}

Pour l’intégration dans le site, j'ai choisi de placer le code dans le fichier */themes/schrek/layouts/_default/single.html*

{{< highlight yalm  >}}

{{ template "_internal/disqus.html" . }}

{{< /highlight >}}

{{< bandeau warning >}} En local ca ne marche pas, il faut envoyer les fichier sur un serveur. {{< / bandeau >}} 


## Liens

https://gohugo.io/content-management/comments/



