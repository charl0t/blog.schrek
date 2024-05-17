---
title: "Installation de Portainer sur Rasp5"
date: 2024-01-15
draft: false
tags: ["RaspberryPi", "Docker","Portainer"]
categories: ["RaspberryPi"]
series: ["RaspberryPi"]
Image: "portainer.webp"
toc: true
---

## Portainer

C'est une application web qui permet de gérer docker via son navigateur.

<!--more-->

## Installation

Comme on a installé Docker précédemment, ca va aller très vite.
Création d'un volume persistent Docker pour garder les données

{{< highlight bash  >}}
$ sudo docker volume create portainer_data
{{< /highlight >}}

Installation de Portainer

{{< highlight bash  >}}
$ sudo docker run -d -p 9000:9000  --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
{{< /highlight >}}

Explications:
run   exécuter un contenaire
\-d  En tache de fond
\-P port d'ecoute
\--restart=always  Redémarre automatiquement le contenaire  https://docs.docker.com/config/containers/start-containers-automatically/
\-v Volume docker
portainer/portainer-ce:latest   Type de contenaire à exécuter

Plus de détailles ici https://docs.docker.com/engine/reference/commandline/run/

On liste les contenaires.

{{< highlight bash  >}}
docker ps
{{< /highlight >}}

Pour y acceder on utilise le port **9000**, par exemple en local 127.0.0.1:9000


## Liens

https://docs.docker.com/engine/install/raspberry-pi-os/
https://raspberrytips.fr/docker-sur-raspberry-pi/



