
---
title: Mon super titre
subtitle: Sous titre
date: \today 
documentclass: scrartcl
papersize: a4
lang: fr-FR
geometry:
- left=2cm
- right=2cm
- top=2cm
- bottom=2cm
colorlinks: true
linkcolor: blue
urlcolor: blue
fontsize: 12pt
toccolor: ProcessBlue
---

# Menu

## Texte

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 


### Gras
Lorem ipsum dolor sit amet, consectetur **adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua**. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 


### Italique
Lorem ipsum dolor sit amet, *consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.* Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

### Barré
~~Lorem ipsum dolor sit amet,~~ Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

### Citations

> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

### Lignes horizontales
___

---

***

## Listes

- Liste1
- Liste 2
- Liste 3

1. Liste 1
2. Liste 2
3. Liste 3

[ ] A
[x] B
[ ] C

## Notes
Footnote 1 link[^first].

Footnote 2 link[^second].

Inline footnote^[Text of inline footnote] definition.

Duplicated footnote reference[^second].

[^first]: Footnote **can have markup**

    and multiple paragraphs.

[^second]: Footnote text.

## Code

C’est le `code, Lorem ipsum dolor sit amet, consectetur`.


``` php
<?php
$var = 20;
echo 'Var='.$var;
?>
```


## Liens

[Lien](https://example.com/ "titre de lien optionnel").

Courriel  <test@example.com>

## Tableau

|cellule 1|cellule 2|
|--------|--------|
|    A    |    B    |
|    C    |    D    |

## Images

![Text alternatif](logo.png "Titre image")




