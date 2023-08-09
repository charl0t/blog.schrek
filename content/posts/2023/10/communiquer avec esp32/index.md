---
title: "Communiquer avec l'Esp32"
date: 2023-10-01
draft: false
tags: ["Esp32","MicroPython","thonny"]
categories: ["IoT"]
series: ["Esp32"]
image: "th.webp"
toc: true
---
Apres avoir installer [Micropython](https://fr.wikipedia.org/wiki/MicroPython) sur notre [Esp32](https://fr.wikipedia.org/wiki/ESP32), il va falloir communiquer avec.

Recevoir les informations, envoyer des fichiers pour le configurer.

Pour cela nous allons utiliser un [environnement de développement](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) ou IDE en anglais.

J'ai choisi [Thonny](https://thonny.org/)

## Installation de Thonny

{{< highlight bash  >}}
$ bash <(curl -s https://thonny.org/installer-for-linux)
{{< /highlight >}}

## Configuration 


## Mon premier code 
{{< highlight python  >}}
# import bibliotheque time et pin
import time
from machine import Pin

print("Bonjour ESP32")
# on defini le pin 2 en sortie (led)
p2 = Pin(2,Pin.OUT)
# faire clignoter la led
while True:
  p2.on()
  time.sleep_ms(500)
  p2.off()
  time.sleep_ms(500)
{{< /highlight >}}


## Liens
https://gcworks.fr/tutoriel/esp/LogicielThonny.html

https://www.upesy.fr/blogs/tutorials/install-micropython-on-esp32-quickly-with-thonny-ide#

https://fr.wikipedia.org/wiki/ESP32

https://fr.wikipedia.org/wiki/MicroPython


{{< chat cactus-comments >}}
