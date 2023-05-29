---
title: "Hugo et les commentaires"
date: 2023-05-20
draft: false
tags: ["Markdown","Html","Hugo","Cactus"]
categories: ["Web"]
series: ["Hugo"]
image: "cactus.wepb"
toc: true
---
{{< figure src="cactus.wepb" title="" width=200px class="imagearticle" >}}

Pas facile de choisir un systeme de commentaire pour [Hugo](https://gohugo.io/content-management/comments/), la facilitée c est [Disqus](https://disqus.com/) avec un template [interne](https://gohugo.io/content-management/comments/#add-disqus).

## Cactus

Mon choix c'est dirigé vers [cactus.chat](https://cactus.chat/), déjà pour la doc qui est facile d'accés et pour [Matrix](https://matrix.org/) qui utilise un protocole ouvert ([Wikipedia](https://fr.wikipedia.org/wiki/Matrix_(protocole))).

## Installation 
C'est bien indiqué [ici](https://cactus.chat/docs/integrations/hugo/).
*The shortcode chat.html must be added to layouts/shortcodes/ and looks like this*

{{< bandeau warning >}} YOUR-SITE-NAME Bien changer cette variable avec le nom de votre site {{< / bandeau >}} 

{{< highlight html>}}
<script type="text/javascript" src="https://latest.cactus.chat/cactus.js"></script>
<link rel="stylesheet" href="https://latest.cactus.chat/style.css" type="text/css">
<div id="comment-section"></div>
<script>
initComments({
  node: document.getElementById("comment-section"),
  defaultHomeserverUrl: "https://matrix.cactus.chat:8448",
  serverName: "cactus.chat",
  siteName: "<YOUR-SITE-NAME>",
  commentSectionId: "{{ index .Params 0 }}"
})
</script>
{{< /highlight >}}

A fin de chaque post on ajoute ce shortcode au fichier md.

{{</* chat cactus-comments */>}}

## Matrix

Sur Linux j'ai choisi [schildi](https://schildi.chat/), il y a pleins d'autres [clients](https://matrix.org/clients/).

Après avoir crée un compte, on va discuter avec @cactusbot:cactus.chat  et lui demander d'enregistrer mon site :

{{< bandeau info >}} c'est le nom que vous avez déclaré a la place de la variable YOUR-SITE-NAME  {{< / bandeau >}} 

{{< highlight html>}}
register schrek.fr    13:32
Created site schrek.fr for you
{{< /highlight >}}

Ensuite, on retourne sur son site et on s'enregistre dans la partie commentaire avec son identifiant Matrix (ça c'est le mien: *@christ0phe:matrix.org* par exemple).


 


## Liens

https://gohugo.io/content-management/comments/

https://cactus.chat/docs/integrations/hugo/

https://matrix.org/




{{< chat cactus-comments >}}
