---
title: "Mealie"
date: 2024-11-18
draft: false
tags: ["Mealie", "Recette","Docker"]
categories: ["Application"]
Image: "mealie.webp"
toc: true
---

Mealie est une application open-source conçue pour centraliser, organiser et partager vos recettes de cuisine. Que vous soyez un chef en herbe ou un passionné de gastronomie cherchant à simplifier la gestion de vos idées culinaires, Mealie propose une interface intuitive et des fonctionnalités puissantes pour créer votre propre bibliothèque numérique de recettes.

<!--more-->

## Principales fonctionnalités de Mealie

### Centralisation des recettes
Mealie vous permet de collecter toutes vos recettes en un seul endroit. Vous pouvez :
* Importer des recettes directement depuis des sites web grâce à un extracteur automatique.
* Ajouter vos propres recettes manuellement, en personnalisant les ingrédients, les étapes, et même les images.

### Planification des repas
Mealie inclut un planificateur de repas interactif. Vous pouvez planifier vos repas à l’avance et générer automatiquement une liste de courses basée sur les ingrédients nécessaires.

### Gestion des ingrédients
L’application offre un outil pour suivre vos ingrédients, vérifier ce que vous avez en stock et éviter le gaspillage alimentaire.

### Partage facile
Mealie facilite le partage de recettes avec vos amis et votre famille grâce à des liens personnalisés ou des fichiers exportables au format PDF.

### Interface utilisateur personnalisable
   * Mode sombre pour un meilleur confort visuel.
   * Catégorisation des recettes par tags, types de cuisine ou préférences alimentaires.
	•	Prise en charge multilingue pour les utilisateurs internationaux.

### Accès multiplateforme
Disponible sur le web, Mealie est accessible depuis n’importe quel appareil doté d’un navigateur. Pour une utilisation plus technique, vous pouvez auto-héberger l’application sur un serveur personnel.



### Comment démarrer avec Mealie ?

* Rendez-vous sur le site officiel de Mealie ou explorez son code source sur GitHub.
* Pour une utilisation basique, accédez à l’application en ligne.
* Si vous préférez héberger l’application, suivez les instructions d’installation pour Docker ou d’autres solutions d’auto-hébergement.

### Exemple de docker compose

{{< highlight docker >}}
services:
  mealie:
    image: ghcr.io/mealie-recipes/mealie:v2.2.0 # 
    container_name: mealie
    restart: always
    ports:
        - "9925:9000"
    deploy:
      resources:
        limits:
          memory: 1000M 
    volumes:
      - mealie-data:/app/data/
    environment:
      # Set Backend ENV Variables Here
      ALLOW_SIGNUP: "false"
      PUID: 1000
      PGID: 1000
      TZ: America/Anchorage
      MAX_WORKERS: 1
      WEB_CONCURRENCY: 1
      # BASE_URL: 

volumes:
  mealie-data:
{{< /highlight >}}


## Liens

https://mealie.io/




