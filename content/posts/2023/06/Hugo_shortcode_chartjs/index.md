---
title: "Shortcode ChartJS"
date: 2023-06-07
tags: ["Shortcode","ChartJS","hugo"]
categories: ["Web"]
image: "chartjs.webp"
toc: true
draft: false
serie : "Hugo"
---

{{< figure src="chartjs.webp" title="" width=200px class="imagearticle" >}}

[ChartJS](https://www.chartjs.org/) est une bibliothèque JavaScript open source gratuite pour la visualisation de données ([Wikipédia](https://fr.wikipedia.org/wiki/Chart.js))

## Le shortcode
J'ai trouvé le code [ici](https://github.com/shen-yu/hugo-chart). 

{{< bandeau danger >}} 
Il y a un problème sur le code (voir [ici](https://discourse.gohugo.io/t/chart-js-not-being-displayed/43172)) 

src="https://cdn.jsdelivr.net/npm/chart.js"
{{< / bandeau >}}

A placer dans le dossier *themes/MONTHEME/layouts/shortcodes/* et à nommer *chart.html*
{{< highlight go-html-template >}}
{{ $w := default "100" (.Get 0) }}
{{ $h := default "300" (.Get 1) }}
{{ $r := ( .Inner | chomp) }}
{{ $seed := "foo" }}
{{ $id := delimit (shuffle (split (md5 $seed) "" )) "" }}

<div style="width: {{ $w }}%;height: {{ $h }}px;margin: 0 auto">
    <canvas id="{{ $id }}"></canvas>
</div>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script type="text/javascript">
    var ctx = document.getElementById('{{ $id }}').getContext('2d');
    var options = {{ $r | safeJS }};
    new Chart(ctx, options);
</script>
{{< /highlight >}}


## Exemple
{{< highlight go-html-template >}}
{{</* chart 90 200 */>}}
{
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: 'Bar Chart',
            data: [12, 19, 18, 16, 13, 14],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
}
{{</* /chart */>}}
{{< /highlight >}}

{{< chart 90 200 >}}
{
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: 'Bar Chart',
            data: [12, 19, 18, 16, 13, 14],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
}
{{< /chart >}}

## Explications
On va prendre un exemple sur le site [ChartJs](https://www.chartjs.org/docs/latest/samples/other-charts/radar.html).

## Squelette de base 
- type: 'radar'

{{< highlight go-html-template >}}
{{</* chart */>}}
{
  type: 'radar',
  data: {},
  options: {}

}
{{</* /chart */>}}
{{< /highlight >}}

## Les données
- Labels: 4 matières (Anglais,Français,Mathématique,Sport)
- datasets: Les notes de l’élève, couleur de fond, fill(remplissage) 
- options: On rajoute un [titre](https://www.chartjs.org/docs/latest/configuration/title.html) 


{{< highlight go-html-template >}}
{{</* chart */>}}
{
  type: 'radar',
  data: {
    labels: ['Anglais','Français','Mathématique','Sport'],
     datasets: [{
    label: 'Note éléve Ducobu',
    data: [12, 10, 14, 18],
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgb(255, 99, 132)',
 }]
},
  options: {},
}

{{</* /chart */>}}
{{< /highlight >}}


{{< chart >}}
{
  type: 'radar',
  data: {
    labels: ['Anglais','Français','Mathématique','Sport'],
     datasets: [{
    label: 'Note éléve Ducobu',
    data: [12, 10, 14, 18],
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgb(255, 99, 132)',
 }]
},
  options: {
    plugins: {
            title: {
                display: true,
                text: 'Note des eleves'
            }
        }
},
}

{{< /chart >}}

## On ajoute un élève

{{< highlight go-html-template >}}
{{</* chart */>}}
{
  type: 'radar',
  data: {
    labels: ['Anglais','Français','Mathématique','Sport'],
     datasets: [{
    label: 'Note élève Ducobu',
    data: [12, 10, 14, 18],
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgb(255, 99, 132)',
 }]
},
  options: {},
}

{{</* /chart */>}}
{{< /highlight >}}


{{< chart 300 500 >}}
{
  type: 'radar',
  data: {
    labels: ['Anglais','Français','Mathématique','Sport'],
     datasets: [{
    label: 'Note élève Ducobu',
    data: [12, 10, 14, 18],
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgb(255, 99, 132)'
 },
    {label: 'Note élève Dupont',
    data: [4, 15, 10, 16],
    fill: true,
    backgroundColor: 'rgba(150, 120, 50, 0.2)',
    borderColor: 'rgb(150, 120, 50)'}

]
},
  options: {
            plugins: {title: {display: true, text: 'Note des eleves'}}
},
}

{{< /chart >}}

## Conclusion
Il faut bien organiser les données dans le fichier, au début c est un peu galére avec toutes les ,[(,)] ...

Mais le resultat est sympa.

## ChartJS generator
Quelques liens pour generer des données 

https://new-ch.art/v1/

https://quickchart.io/chart-maker/

## Liens

https://github.com/shen-yu/hugo-chart

https://www.chartjs.org/

https://ordinarycoders.com/blog/article/11-chart-js-examples


{{< chat cactus-comments >}}
