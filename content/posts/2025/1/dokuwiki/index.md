---
title: "Dokuwiki"
date: 2025-01-20
draft: false
tags: ["Dokuwiki","Docker"]
categories: ["Logiciel"]
Image: "docuwiki.webp"
toc: true
---

DokuWiki est un logiciel de gestion de contenu open source conçu pour créer et gérer des wikis. Connu pour sa simplicité et son efficacité, il s’adresse aussi bien aux utilisateurs débutants qu’aux professionnels cherchant une solution robuste et légère.

<!--more-->


## Fonctionnalités principales

- Facilité d’utilisation : DokuWiki utilise une syntaxe simple basée sur du texte brut, rendant la création et la modification de pages intuitive, sans besoin de bases en HTML.
- Sans base de données : Contrairement à de nombreux CMS, il stocke les données dans des fichiers texte, ce qui simplifie l’installation et la maintenance.
- Extensibilité : Grâce à une grande variété de plugins et de thèmes, il est possible d’adapter DokuWiki à des besoins spécifiques.
- Contrôle des révisions : Chaque modification est enregistrée, permettant de suivre les changements et de restaurer des versions antérieures facilement.
- Communauté active : Avec une documentation riche et une communauté dynamique, le support et les ressources sont facilement accessibles.



DokuWiki est idéal pour la documentation, les intranets, les manuels ou toute situation nécessitant une collaboration efficace. Sa légèreté et son approche sans base de données en font une solution pratique pour les projets de toutes tailles.



## Installation avec Docker-compose
```
services:
  dokuwiki:
    image: lscr.io/linuxserver/dokuwiki:latest
    container_name: dokuwiki
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - .dokuwiki/config:/config
    ports:
      - 7500:80
    restart: unless-stopped
volumes:
  dokuwiki:
```

## 1er configuration 
- Connectez vous sur l’IP

```http://$IP:$PORT/install.php```

Exemple: 192.168.1.34:7500

## Liens

https://www.dokuwiki.org/dokuwiki

https://docs.linuxserver.io/images/docker-dokuwiki/

