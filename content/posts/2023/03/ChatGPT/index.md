---
title: "ChatGPT dans un terminal"
date: 2023-03-30
draft: false
tags: ["ChatGpt"]
categories: ["Web"]
image: "chatgpt_logo.webp"
toc: true
---
{{< figure src="chatgpt_logo.webp" title="" width=200px class="imagearticle" >}}

[ChatGPT](https://fr.wikipedia.org/wiki/ChatGPT), le célèbre générateur de texte contrôlé par une intelligence artificielle , peut être utilisé dans un terminal.

##API key:

Il faut créer un compte et générer une API KEY [ici](https://platform.openai.com/account/api-keys).
ça sera sur la forme.

{{< highlight bash >}}
 sk-qUP3OL6jQ95cXJbxsxyPT3BlbkFJzf3ypT6djfo2ZsjcZwME2
{{< / highlight >}}

## Le script
Tout ce trouve sur ce [github](https://github.com/0xacx/chatGPT-shell-cli).

{{< highlight bash >}}
$ wget https://github.com/0xacx/chatGPT-shell-cli/blob/main/chatgpt.sh
$ chmod +x chatgpt.sh 
$ export OPENAI_KEY=sk-qUP3OL6jdkdlQ95cXJbxsxyPT3Bldkkkff3ypT6Rn1gZsjcZwME2
{{< / highlight >}}

Remplacez OPENAI_KEY par votre clef.

Le script a besoin de jq.

{{< highlight bash >}}
$ sudo apt install jq
{{< / highlight >}}

et pour finir:
 
{{< highlight bash >}}
$ ./chatgpt.sh 
Welcome to chatgpt. You can quit with 'exit' or 'q'.

Enter a prompt:
bonjour

chatgpt Bonjour! Comment puis-je vous aider aujourd'hui?

Enter a prompt:
une blague sur les chats

chatgpt Bien sûr! Voici une blague sur les chats :

Pourquoi les chats n'aiment-ils pas jouer au poker dans la jungle ?
Parce qu'il y a trop de léopards !
{{< / highlight >}}

## Lien

https://github.com/0xacx/chatGPT-shell-cli


