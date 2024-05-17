---
title: "Shortcode Codepen"
date: 2023-05-25
draft: false
tags: ["Shortcode", "Codepen","Hugo"]
categories: ["Web"]
series: ["Hugo"]
image: "codepen-logo-8.png"
toc: true
---
{{< figure src="codepen-logo-8.png" title="" width=200px class="imagearticle" >}}

On va creer notre shortcode pour le site [Codepen](https://codepen.io/), ca qui va nous permetre l'afficher dans Hugo.

## Le code 
Sur le site de Codepen, dans l'onglet embeb on va trouver le code Html pour l'integrer sur un site. 

{{< highlight html >}}
<p class="codepen" data-height="300" data-theme-id="light" data-default-tab="html,result" data-slug-hash="YzObPmg" data-user="christ0phe" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/christ0phe/pen/YzObPmg">
  Purecss</a> by christophe (<a href="https://codepen.io/christ0phe">@christ0phe</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
{{< /highlight >}}

## Le Shortcode
Dans le lien de Codepen on a l'identifiant a la fin  *YzObPmg* 

https://codepen.io/christ0phe/pen/YzObPmg

{{< highlight go-html-template >}}
{{</* codepen code */>}}  
{{< /highlight >}}

{{< highlight go-html-template >}}
<!--
https://codepen.io/
-->
<p class="codepen" data-height="300" data-theme-id="light" data-default-tab="html,result" data-slug-hash="{{- .Get 0 -}}"" data-user="christ0phe" style="height: 400px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>Voir le pen <a href="https://codepen.io/christ0phe/pen/{{- .Get 0 -}}"">
  Purecss</a> by christophe (<a href="https://codepen.io/christ0phe">@christ0phe</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
{{< /highlight >}}

## Résultat

{{</* codepen YzObPmg */>}}  

{{< codepen YzObPmg >}}

## Liens

https://kinson.io/post/embed-codepen/



