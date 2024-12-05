---
title: "Duckdns et Caddy"
date: 2025-02-01
draft: false
tags: ["Caddy","Duckdns"]
categories: ["Logiciel"]
Image: "duck.webp"
toc: true
---
DuckDNS est un service gratuit et open source de DNS dynamique (Dynamic DNS) qui permet d’associer une adresse IP dynamique à un nom de domaine fixe. Idéal pour les utilisateurs ayant des connexions Internet avec des adresses IP changeantes, DuckDNS simplifie l’accès à des serveurs ou des services auto-hébergés.

## Fonctionnement

DuckDNS fonctionne en actualisant automatiquement l’adresse IP associée à un domaine personnalisé (souvent en sous-domaine de duckdns.org). Cela se fait grâce à des scripts ou des intégrations dans des routeurs, serveurs ou services comme Linux, Windows, ou Docker.

## Mon problème 
J’aimerais pouvoir accéder aux services que j’installe sur mon Raspberry-Pi. 
J’ai des services sur différents ports dans Docker et un serveur Apache qui tourne sur le port 80


## Installation 

### Box internet 
Il faut rediriger le port 80 sur le Raspberry-Pi via le nappage des ports.

### Duckdns
Après s’être enregistré sur le site duckdns.org, on va créer un nom de domaine et récupérer le Token.

Exemple:
- Account memepasmal@gmail.com
- type free
- token 1a72a174-5766-424e-ae8e-6c5dcc4a03a8

L’installation sur le Raspberry ne pose pas de problème https://www.duckdns.org/install.jsp

### Caddy
Maintenant que le nom de domaine pointé sur mon installation, il va falloir rediriger les requêtes vers les différents ports via Caddy qui va servir de reverse-proxy.

https://fr.wikipedia.org/wiki/Proxy_inverse

Il va valoir ajouter au logiciel Caddy le fournisseur duckdns 

https://caddyserver.com/docs/modules/dns.providers.duckdns

### Installation de Xcaddy 

``` bash
$ sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
$ curl -1sLf 'https://dl.cloudsmith.io/public/caddy/xcaddy/gpg.key' | sudo gpg --dearmor -o 
/usr/share/keyrings/caddy-xcaddy-archive-keyring.gpg
$ curl -1sLf 'https://dl.cloudsmith.io/public/caddy/xcaddy/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-xcaddy.list
$ sudo apt update
$ sudo apt install xcaddy
``` 

### Construction de Caddy avec Xcaddy

``` bash
$ xcaddy build --with github.com/caddy-dns/duckdns
```

### Sauvegarde et mise en place du binaire

``` bash
$ sudo mv /usr/bin/caddy /usr/bin/caddy.old
$ sudo cp caddy /usr/bin/
```

### Configuration

``` bash
$ sudo nano /etc/caddy/Caddyfile
```
On édite le fichier *Caddyfile*, ensuite il faut mettre votre propre **TOKEN DuckDNS**, votre **Nom de domaine**, et l'IP du service Docker
``` yaml
https://apache.test.duckdns.org {
        reverse_proxy localhost:4433
        tls {
                dns duckdns zd465-zd65-zfdf5-df5z-456814df
                propagation_timeout 2m
                propagation_delay 2m
        }
}
``` 

### Correction et lancement de CADDY

``` bash
$ sudo caddy fmt --overwrite /etc/caddy/Caddyfile
$ sudo caddy start --config /etc/caddy/Caddyfile
``` 


