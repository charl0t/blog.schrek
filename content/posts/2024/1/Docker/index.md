---
title: "Docker avec un RaspberryPi 5"
date: 2024-01-10
draft: false
tags: ["RaspberryPi", "Docker"]
categories: ["RaspberryPi"]
series: ["RaspberryPi"]
Image: "docker.webp"
toc: true
---

## Docker:

Docker est une plateforme permettant de lancer certaines [applications](https://fr.wikipedia.org/wiki/Application_\(informatique\)) dans des conteneurs. C'est différent des  machines virtuels et ca utilise moins de ressource.

<!--more-->

## Installation:

On fait la mise a jour du système, cela permet de partir propre.

{{< highlight bash  >}}
$ sudo apt update
$ sudo apt upgrade
{{< /highlight >}}

Installation a l'aide du script officiel.

{{< highlight bash  >}}
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
{{< /highlight >}}

Apres quelques minutes, on regarde si ca tourne.

{{< highlight bash  >}}
$ sudo systemctl status docker
{{< /highlight >}}

On ajoute l'utilisateur **pi** a docker.

{{< highlight bash  >}}
$ sudo usermod -aG docker pi
{{< /highlight >}}

L'installation ne pose pas de problèmes particuliers.


## Liens

https://docs.docker.com/engine/install/raspberry-pi-os/

https://raspberrytips.fr/docker-sur-raspberry-pi/



