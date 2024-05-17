---
title: "Diceware"
date: 2023-02-24
draft: false
tags: ["Linux","Mots de passe"]
categories: ["Web"]
image: "one-red-dice-01-a9bf3.webp"
toc: true
---
{{< figure src="one-red-dice-01-a9bf3.webp" title="" width=200px class="imagearticle" >}}

C est fini les mots de passe, il faut passer aux phrases de passe.
Plus facile à retenir plus compliquer à casser.
Pour les mots de passe, l’avantage est que l’on peut décomplexifier un mot de passe avec tous les caractères 
{{< highlight bash >}}
MaisonBananeRougeMystereBiere 
AhdikeJeujenksKjnskodnKshjkskk
{{< /highlight >}}

{{< figure src="diceware.png-369a6.webp" title="" width=600px class="imagearticle" >}}

Pour générer une phrase de passe il faut un outil qui crée du « hasard » et un dictionnaire de mot qui va bien.

## Qu’est-ce que  Diceware ?
Diceware est une méthode pour construire une phrase de passe qui utilise des dés pour choisir au hasard des mots parmi une liste.
Chaque mot de la liste est précédé par un nombre à cinq chiffres. 
On lance un dé cinq fois ou une fois cinq dés, le résultat donne un mot dans la liste.

<!-- more -->

Exemple de liste:
{{< highlight bash >}}
32424 gaule
32425 gava
32426 gavais
32431 gavant
32432 gave
32433 gavee
32434 gaves
32435 gavez
32436 gavial
32441 gaviez
{{< /highlight >}}

Pour l’outil, on va utiliser Diceware et pour les mots des dictionnaires.

## L’outil


[Diceware](https://github.com/ulif/diceware) en ligne de commande.
L’utilisation est simple 

{{< highlight bash >}}
 $ diceware -h Aide
 $ diceware dictionnaire.txt Utilise la liste des mots du dico
{{< /highlight >}}
{{< highlight bash >}}
-n nombre de mots
-c Majuscule au début de chaque mot (par défaut)
--no-caps Sans majuscule
-s NUM Insérer des caractères spéciaux NUM: nombre de caractère 
-d DELIMITER Insérer un séparateur de mot 
{{< /highlight >}}

## Un exemple 

{{< highlight bash >}}
$ diceware -d \& -n 4 wordlist_fr_4d_2.txt 
Personne&Dangereux&Myrtille&Moderne
{{< /highlight >}}

{{< highlight bash >}}
\# pour échapper le caractère spécial, sinon ça déclenche une erreur
{{< /highlight >}}


## Les dictionnaires

https://github.com/chmduquesne/diceware-fr

https://github.com/mbelivo/diceware-wordlists-fr

## Liens

https://fr.wikipedia.org/wiki/Diceware

https://github.com/ulif/diceware

https://github.com/mbelivo/diceware-wordlists-fr

http://world.std.com/~reinhold/diceware.html

https://connect.ed-diamond.com/MISC/MISC-080/Mots-de-passe-le-mieux-est-l-ennemi-du-bien

https://diceware.readthedocs.io/en/stable/wordlists.html




