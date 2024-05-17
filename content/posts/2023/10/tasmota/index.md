---
title: "Tasmota"
date: 2023-10-01
draft: false
tags: ["Esp32","Tasmota","Esp8266"]
categories: ["IoT"]
series: ["Domotique"]
image: "tasmota.webp"
toc: true
---
[Tasmota](https://tasmota.github.io/docs/) est un firmware OpenSource pour des appareils basé sur des ESP8266.
Il va permetre de faire communiquer facilement vos projets domotiques.

## Installation

Il existe plusieurs façon de [flasher](https://tasmota.github.io/docs/Getting-Started/), on va choisir la plus simple. 

On va prendre un simple [Wemos d1 mini](https://amzn.to/44DoB1W) pour l'exemple.

Il faut brancher en Usb sur le pc et on ouvre la page [https://tasmota.github.io/install/](https://tasmota.github.io/install/)

{{< bandeau warning >}} Il faut utiliser Chrome comme navigateur pour etablir la liaison. {{< / bandeau >}} 

Choisir ESP8266  et Fr 

{{< figure src="tasmota1.webp" title="" width=400px class="imagearticle" >}}

Tous ca marche avec tous les ESP, il reste juste à brancher des sondes dessus mais ca fera partie d'un autre épisode.

On branche l'ESP sur le port USN et on regarde ou il est monté.

{{< highlight bash  >}}
$ dmesg
[ 7991.018239] usb 1-3: ch341-uart converter now attached to ttyUSB0
{{< /highlight >}}

On va choisi le bon port de connection, ici c est *ttyUSB0*.

{{< figure src="1.webp" title="" width=400px class="imagearticle" >}}

Installation du microcode.

{{< figure src="2.webp" title="" width=400px class="imagearticle" >}}

{{< figure src="3.webp" title="" width=400px class="imagearticle" >}}

{{< figure src="4.webp" title="" width=400px class="imagearticle" >}}

Configuration du wifi. 

{{< figure src="5.webp" title="" width=400px class="imagearticle" >}}

{{< figure src="6.webp" title="" width=400px class="imagearticle" >}}

Et voila c'est tous, la prochaine etapes c'est interagir avec.

{{< figure src="7.webp" title="" width=400px class="imagearticle" >}}

## Liens
https://tasmota.github.io/docs/

https://gladysassistant.com/fr/docs/integrations/tasmota/

https://lofurol.fr/joomla/electronique/domotique/317-tasmota-flasher-un-module-esp-32-lolin32-lite

