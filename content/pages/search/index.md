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
   
