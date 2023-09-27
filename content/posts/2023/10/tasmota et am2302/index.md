---
title: "Tasmota et AM2302"
date: 2023-10-15
draft: false
tags: ["AM2302","Tasmota","Esp8266"]
categories: ["IoT"]
series: ["Domotique"]
image: "am2302.webp"
toc: true
---

Maintenant que l'on sait installer Tasmota sur un Wemos, il va falloir interagir avec.
On va utiler des composants simples.

- [Wemos d1 mini](https://amzn.to/3sWyOJP) 
- [AM2302](https://amzn.to/3Pip2ZY)
- [Une platine d'essais](https://amzn.to/467jkRk)

## AM2302

Il s'agit d'un capteur numérique de température et d'humidité de base à faible coût.
Le capteur mesure les données de l'air environnant et les transmet sous forme de signal numérique à la broche de données. 

## Le branchement 
{{< bandeau danger >}} On branche pas encore le wemos en USB  {{< / bandeau >}} 

Rien de bien compliqué

{{< figure src="wemos.webp" title="" width=400px class="imagearticle" >}}

{{< figure src="wemos_am2302.webp" title="" width=600px class="imagearticle" >}}

{{< figure src="wemos_am2302_shema.webp" title="" width=600px class="imagearticle" >}}

## Configuration de Tasmota

Aprés avoir tous connecté et verifié, on va connecter notre wemos en usb sur le pc et nous connecter sur l'adresse IP de notre wemos avec Tasmota dessus.

{{< figure src="tasmota.webp" title="" width=300px class="imagearticle" >}}



## Liens

{{< chat cactus-comments >}}
