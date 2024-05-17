---
title: "Afficher Latex dans Hugo"
date: 2023-06-01
tags: ["Latex","Hugo","Shortcode"]
categories: ["Web"]
image: "latex.webp"
toc: true
series: ["Hugo"]
draft: false
---
{{< figure src="latex.webp" title="" width=200px class="imagearticle" >}}


## Le shortcode
Fichier *latex.html* à deposer */themes/VOTRETHEME/layouts/shortcodes*

{{< highlight go-html-template >}}
  <script type="module">
    import { LaTeXJSComponent } from "https://cdn.jsdelivr.net/npm/latex.js/dist/latex.mjs"
    customElements.define("latex-js", LaTeXJSComponent)
  </script>

  <style>
    latex-js {
      display: inline-block;
      width: 70%;
      border: 1px solid black;
      margin-right: 2em;
      padding-bottom: 2em;
    }
  </style>

  <latex-js baseURL="https://cdn.jsdelivr.net/npm/latex.js/dist/">
{{ .Inner }}
</latex-js>
{{< /highlight >}}

{{< bandeau success >}} {{ .Inner }} permet d'inserer tous ce qu'il se trouve entre les balises.{{< / bandeau >}} 

## Utilisation

{{< highlight go-html-template >}}
{{</* latex */>}}
\documentclass{article}
\usepackage[latin1]{inputenc}
\usepackage{hyperref}
\author{Christophe}
\date{2023}
\title{Un exemple}
\usepackage[francais]{babel}
\begin{document}
\maketitle
\section{Début}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
\section{Suite}
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
\section{Fin}
Egestas integer eget aliquet nibh praesent tristique magna sit amet. Accumsan lacus vel facilisis volutpat est velit egestas dui id. 
Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque
\section{Source}
The source of \LaTeX.js is here on GitHub: \url{https://github.com/michael-brade/LaTeX.js}
\end{document}
{{</* /latex */>}}
{{< /highlight >}}

{{< latex >}}
\documentclass{article}
\usepackage[latin1]{inputenc}
\usepackage{hyperref}
\author{Christophe}
\date{2023}
\title{Un exemple}
\usepackage[francais]{babel}
\begin{document}
\maketitle
\section*{Début}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
\section*{Suite}
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
\section*{Fin}
Egestas integer eget aliquet nibh praesent tristique magna sit amet. Accumsan lacus vel facilisis volutpat est velit egestas dui id. 
Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque
\section*{Source}
The source of \LaTeX.js is here on GitHub: \url{https://github.com/michael-brade/LaTeX.js}
\end{document}
{{< /latex >}}

## Exemple

https://latex.js.org/playground.html

{{< latex >}}
\documentclass{article}

\usepackage{comment, multicol}
\usepackage{hyperref}

\usepackage{calc,pict2e,picture}
\usepackage{textgreek,textcomp,gensymb,stix}

\setcounter{secnumdepth}{2}

\title{\LaTeX.js Showcase}
\author{made with $\varheartsuit$ by Michael Brade}
\date{2017--2021}

\begin{document}

\maketitle


\begin{abstract}
This document will show most of the features of \LaTeX.js while at the same time being a gentle introduction to \LaTeX.
In the appendix, the API as well as the format of custom macro definitions in JavaScript will be explained.
\end{abstract}


\section{Characters}

It is possible to input any UTF-8 character either directly or by character code
using one of the following:

\begin{itemize}
    \item \texttt{\textbackslash symbol\{"00A9\}}: \symbol{"00A9}
    \item \verb|\char"A9|: \char"A9
    \item \verb|^^A9 or ^^^^00A9|: ^^A9 or ^^^^00A9
\end{itemize}

\bigskip

\noindent
Special characters, like those:
\begin{center}
\$ \& \% \# \_ \{ \} \~{} \^{} \textbackslash % \< \>  \"   % TODO cannot be typeset
\end{center}
%
have to be escaped.

More than 200 symbols are accessible through macros. For instance: 30\,\textcelsius{} is
86\,\textdegree{}F. See also Section~\ref{sec:symbols}.



\section{Spaces and Comments}

Spaces and comments, of course, work just as they do in \LaTeX.
This is an            % stupid
% Better: instructive <----
example: Supercal%
                ifragilist%
    icexpialidocious

It does not matter whether you enter one or several     spaces after a word, it
will always be typeset as one space---unless you force several spaces, like\ \ now.

New \TeX users may miss whitespaces after a command. % renders wrong
Experienced \TeX{} users are \TeX perts, and know how to use whitespaces. % renders correct

Longer comments can be embedded in the \texttt{comment} environment:
This is another  \begin  {comment}
rather stupid,
but helpful
\end
{comment}
example for embedding comments in your document.



\section{Dashes and Hyphens}

\LaTeX\ knows four kinds of dashes. Access three of them with different numbers
of consecutive dashes. The fourth sign is actually not a dash at all---it is the
mathematical minus sign:

\begin{quote}
    daughter-in-law, X-rated\\
    pages 13--67\\
    yes---or no? \\
    $0$, $1$ and $-1$
\end{quote}
%
The names for these dashes are: ‘-’ hyphen, ‘--’ en-dash, ‘---’ em-dash,
and ‘$-$’ minus sign. \LaTeX.js outputs the actual true unicode character for those
instead of using the hypen-minus.



\section{Text and Paragraphs, Ligatures}

An empty line starts a new paragraph, and so does \verb|\par|.
\par Like this. A new line usually starts automatically when the previous one is
full. However, using \verb+\newline+ or \verb|\\|,\newline one can force \\ to start a new line.

Ligatures are supported as well, for instance:

\begin{center}
fi, fl, ff, ffi, ffl \dots{} instead of f\/i, f\/l, f\/f\/l \dots
\end{center}

Use \texttt{\textbackslash\slash} to prevent a ligature.



\begin{multicols}{2}[\subsection{Multicolumns}]

The multi-column layout, using the \texttt{multicols} environment, allows easy
definition of multiple columns of text---just like in newspapers. The first
and mandatoriy argument specifies the number of columns the text should be divided into.

It is often convenient to spread some text over all columns, just before the multicolumn
output. In \LaTeX, this was needed to prevent any page break in between. To achieve this,
the \texttt{multicols} environment has an optional second argument which can be used for
this purpose.

For instance, this text you are reading now was started with the argument
\texttt{\textbackslash subsection\{Multicolumns\}}.

\end{multicols}
\end{document}
{{< /latex >}}


## Possibilités
https://latex.js.org/playground.html

## Limitations
https://latex.js.org/limitations.html


## Liens
https://latex.js.org/

https://fr.wikibooks.org/wiki/LaTeX

https://zestedesavoir.com/tutoriels/826/introduction-a-latex/

https://www.learnlatex.org/fr/
