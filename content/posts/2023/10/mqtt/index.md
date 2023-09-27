---
title: "MQTT"
date: 2023-10-25
draft: false
tags: ["MQTT","Domotique","Tasmota","Home-assistant"]
categories: ["IoT"]
series: ["Domotique"]
image: "mqtt.webp"
toc: true
---

Créé par Andy Stanford-Clark et Arlen Nipper en 1999, MQTT est un protocole de messagerie qui permet aux objets connectés d’échanger les informations en toutes sécurité et avec une faible bande passante.

## Les termes utilisés

- Broker: c'est le programme qui centralise les informations, il reçoit et envoie des messages comme la température d'un capteur. Le broker de référence sous Linux s’appelle [Mosquitto](https://mosquitto.org/).
- Publish: c'est l'action d'envoyer l'information du capteur vers le Broker( programme).
- Subscribe: c'est quand un programme s'abonne a un broker pour recuperer des informations.
- Topic: c'est les rubriques ou sont classés les données par exemple *esp32/maison/chambre*. 

## QoS (Quality Of Service )
MQTT possede 3 niveau de qualité de service:

Pour chaque topic, MQTT permet de gérer la QoS désirée, les messages seront délivrés :

- QoS 0 : Une fois au plus
- QoS 1 : Une fois au moins
- QoS 2 : Exactement une seule fois

## Fonctionnement 

{{< figure src="mqtt-architecture.webp" title="" width=400px class="imagearticle" >}}

Exemple d'envoi
{{< highlight bash  >}}
16:31:08.375 MQT: stat/tasmota_63753D/STATUS2 = {"StatusFWR":{"Version":"13.1.0.2(tasmota)","BuildDateTime":"2023-09-03T16:37:03","Boot":31,"Core":"2_7_4_9","SDK":"2.2.2-dev(38a443e)","CpuFrequency":80,"Hardware":"ESP8266EX","CR":"396/699"}}
16:31:08.427 MQT: stat/tasmota_63753D/STATUS10 = {"StatusSNS":{"Time":"2023-09-18T16:31:08","AM2301":{"Temperature":27.4,"Humidity":68.0,"DewPoint":21.0},"TempUnit":"C"}}
{{< /highlight >}}

## Configuration avec Tasmota
J'ai repris le montage de l'article précedent avec le AM2301 comme capteur.

Rien de compliqué, on active MQTT.
{{< figure src="tasmota1.webp" title="" width=400px class="imagearticle" >}}
Et on le configure.
{{< figure src="tasmota2.webp" title="" width=400px class="imagearticle" >}}

## Configuration Home-assistant


- On va créer un utilisateur dans home assistant par exemple mosquitto avec un mot de passe compliqué 
- On ajoute le module [Mosquitto](https://www.home-assistant.io/integrations/mqtt/).
 
Dans Parametres --> Modules complementaire --> Boutique des modules complementaires.

Le paramétrage est [facile](https://devotics.fr/installer-mqtt-sur-home-assistant/). 

Ensuite, on va creer notre capteur(sensor) qui va recuperer les infos, à ajouter dans votre *configuration.yaml*.

(Voir la section MQTTexplorer pour le chemin )

{{< highlight bash  >}}
  - sensor:
      name: "tmp_solaire"
      unique_id: "tmp_solaire"
      state_topic: "tele/tasmota_63753D/SENSOR"
      device_class: "Temperature"
      unit_of_measurement: "C"
      value_template: '{{ value_json.AM2301.Temperature }}'
{{< /highlight >}}

## MQTTexplorer

Avec [mqtt-explorer](https://mqtt-explorer.com/), on peut verifier les données qui sont sur le broker.

Surtout le chemin pour completer *state_topic* et *value_template* dans Home-Assistant.
 
{{< figure src="mqttexplorer.webp" title="" width=400px class="imagearticle" >}}

## Résultat dans home-assistant

{{< figure src="home.webp" title="" width=400px class="imagearticle" >}}

## Liens
https://fr.wikipedia.org/wiki/MQTT

https://aws.amazon.com/fr/what-is/mqtt/

https://fr.linkedin.com/pulse/mqtt-expliqu%C3%A9-en-fran%C3%A7ais-rapha%C3%ABl-delstanche

https://mosquitto.org/

https://devotics.fr/installer-mqtt-sur-home-assistant/



{{< chat cactus-comments >}}
