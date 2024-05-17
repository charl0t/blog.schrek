---
title: "Hugo et Pwa"
date: 2023-09-20
draft: false
tags: ["Liens","Hugo","Pwa"]
categories: ["Web"]
series: ["Hugo"]
image: "pwa.webp"
toc: true
---

Le PWA (Progressive Web App) permet de faire ressembler un site a une application.

<!--more-->

## Mode hors ligne
Le squelette de la page *Hors ligne*

*/themes/VOTRETHEME/layouts/_default/hors_ligne.html*

{{< highlight go-html-template  >}}
<html>
 <head>
  <title>{{ .Title }}</title>
 </head>
 <body>
    <h1>{{ .Title }}</h1>
    {{ .Content }}
 </body>
</html>
{{< /highlight >}}

La page *Hors ligne*

*/pages/hors_ligne/index.md*

{{< highlight go-html-template >}}
---
title: "Hors ligne"
date: 2023-04-07
layout: hors_ligne
toc: false
---
**Hors ligne**
{{</*  figure src="wifi.png" title="" width=100px */>}} 

{{< /highlight >}}


## Les icônes
Pour générer plusieurs icônes j'ai utilisé ce service [Favicon-generetor](https://www.favicon-generator.org/).
Il doit y en avoir d'autres sur le web.
Ensuite, on les place dans ce dossier.

*/themes/VOTRETHEME/static/img/favicons/*

{{< highlight bash >}}
── logo-128x128.png
├── logo-144x144.png
├── logo-152x152.png
├── logo-256x256.png
├── logo-512x512.png
├── logo-72x72.png
└── logo-92x92.png
{{< /highlight >}}

## Manifest.json
Maintenant, il faut remplir le [manifest](https://pwa-workshop.js.org/fr/1-manifest/#proprietes-du-manifeste) avec vos données et vos icônes.

On le place dans le dossier *static* de votre théme.

*/themes/VOTRETHEME/static/manifest.json*

{{< highlight json >}}
{
  "lang": "fr",
  "name": "Schrek.fr",
  "short_name": "schrek.fr",
  "description": "Mon super site avec Hugo",
  "icons": [
{
    "src": "/img/favicons/logo-72x72.png",
    "sizes": "72x72",
    "type": "image/png"
  }, {
    "src": "/img/favicons/logo-92x92.png",
    "sizes": "92x92",
    "type": "image/png"
  }, {
    "src": "/img/favicons/logo-128x128.png",
    "sizes": "128x128",
    "type": "image/png"
  }, {

    "src": "/img/favicons/logo-144x144.png",
    "sizes": "144x144",
    "type": "image/png"
  }, {
    "src": "/img/favicons/logo-152x152.png",
    "sizes": "152x152",
    "type": "image/png"
  }, {
    "src": "/img/favicons/logo-256x256.png",
    "sizes": "256x256",
    "type": "image/png"
    }, {
    "src": "/img/favicons/logo-512x512.png",
    "sizes": "512x512",
    "type": "image/png"
  }],

  "start_url": "/",
  "display": "standalone",
  "orientation" : "portrait",
  "background_color": "#000000",
  "theme_color": "#000000"
}
{{< /highlight >}}

## Le service worker
Une explication sur le site de [mozilla](https://developer.mozilla.org/fr/docs/Web/API/Service_Worker_API/Using_Service_Workers) de son rôle.

Je suis partie de ce depot [Git](https://github.com/wildhaber/offline-first-sw/tree/master) que j'ai personnalisé.

{{< highlight js >}}
const CACHE_VERSION = 1.1;

const BASE_CACHE_FILES = [
    '/style.css',
    '/uikit.min.js',
    'uikit-icons.min.js',
    '/manifest.json',
    '/favicon.png',
    '/index.json',
];

const OFFLINE_CACHE_FILES = [
    '/style.css',
    '/script.js',
    '/pages/hors_ligne/index.html',
];

const NOT_FOUND_CACHE_FILES = [
    '/style.css',
    '/uikit.min.js',
    'uikit-icons.min.js',
    '/404.html',
    '/pages/hors_ligne/index.html',
];

const OFFLINE_PAGE = '/pages/hors_ligne/index.html';
const NOT_FOUND_PAGE = '/404.html';

const CACHE_VERSIONS = {
    assets: 'assets-v' + CACHE_VERSION,
    content: 'content-v' + CACHE_VERSION,
    offline: 'offline-v' + CACHE_VERSION,
    notFound: '404-v' + CACHE_VERSION,
};

// Define MAX_TTL's in SECONDS for specific file extensions
const MAX_TTL = {
    '/': 3600,
    html: 3600,
    json: 86400,
    js: 86400,
    css: 86400,
};

const CACHE_BLACKLIST = [
    //(str) => {
    //    return !str.startsWith('https://schrek.fr') ;
    //},
];

const SUPPORTED_METHODS = [
    'GET',
];

/**
 * isBlackListed
 * @param {string} url
 * @returns {boolean}
 */
function isBlacklisted(url) {
    return (CACHE_BLACKLIST.length > 0) ? !CACHE_BLACKLIST.filter((rule) => {
        if(typeof rule === 'function') {
            return !rule(url);
        } else {
            return false;
        }
    }).length : false
}

/**
 * getFileExtension
 * @param {string} url
 * @returns {string}
 */
function getFileExtension(url) {
    let extension = url.split('.').reverse()[0].split('?')[0];
    return (extension.endsWith('/')) ? '/' : extension;
}

/**
 * getTTL
 * @param {string} url
 */
function getTTL(url) {
    if (typeof url === 'string') {
        let extension = getFileExtension(url);
        if (typeof MAX_TTL[extension] === 'number') {
            return MAX_TTL[extension];
        } else {
            return null;
        }
    } else {
        return null;
    }
}

/**
 * installServiceWorker
 * @returns {Promise}
 */
function installServiceWorker() {
    return Promise.all(
        [
            caches.open(CACHE_VERSIONS.assets)
                .then(
                    (cache) => {
                        return cache.addAll(BASE_CACHE_FILES);
                    }
                ),
            caches.open(CACHE_VERSIONS.offline)
                .then(
                    (cache) => {
                        return cache.addAll(OFFLINE_CACHE_FILES);
                    }
                ),
            caches.open(CACHE_VERSIONS.notFound)
                .then(
                    (cache) => {
                        return cache.addAll(NOT_FOUND_CACHE_FILES);
                    }
                )
        ]
    )
        .then(() => {
            return self.skipWaiting();
        });
}

/**
 * cleanupLegacyCache
 * @returns {Promise}
 */
function cleanupLegacyCache() {

    let currentCaches = Object.keys(CACHE_VERSIONS)
        .map(
            (key) => {
                return CACHE_VERSIONS[key];
            }
        );

    return new Promise(
        (resolve, reject) => {

            caches.keys()
                .then(
                    (keys) => {
                        return legacyKeys = keys.filter(
                            (key) => {
                                return !~currentCaches.indexOf(key);
                            }
                        );
                    }
                )
                .then(
                    (legacy) => {
                        if (legacy.length) {
                            Promise.all(
                                legacy.map(
                                    (legacyKey) => {
                                        return caches.delete(legacyKey)
                                    }
                                )
                            )
                                .then(
                                    () => {
                                        resolve()
                                    }
                                )
                                .catch(
                                    (err) => {
                                        reject(err);
                                    }
                                );
                        } else {
                            resolve();
                        }
                    }
                )
                .catch(
                    () => {
                        reject();
                    }
                );

        }
    );
}

function precacheUrl(url) {
    if(!isBlacklisted(url)) {
        caches.open(CACHE_VERSIONS.content)
            .then((cache) => {
                cache.match(url)
                    .then((response) => {
                        if(!response) {
                            return fetch(url)
                        } else {
                            // already in cache, nothing to do.
                            return null
                        }
                    })
                    .then((response) => {
                        if(response) {
                            return cache.put(url, response.clone());
                        } else {
                            return null;
                        }
                    });
            })
    }
}



self.addEventListener(
    'install', event => {
        event.waitUntil(
            Promise.all([
                installServiceWorker(),
                self.skipWaiting(),
            ])
        );
    }
);

// The activate handler takes care of cleaning up old caches.
self.addEventListener(
    'activate', event => {
        event.waitUntil(
            Promise.all(
                [
                    cleanupLegacyCache(),
                    self.clients.claim(),
                    self.skipWaiting(),
                ]
            )
                .catch(
                    (err) => {
                        event.skipWaiting();
                    }
                )
        );
    }
);

self.addEventListener(
    'fetch', event => {

        event.respondWith(
            caches.open(CACHE_VERSIONS.content)
                .then(
                    (cache) => {

                        return cache.match(event.request)
                            .then(
                                (response) => {

                                    if (response) {

                                        let headers = response.headers.entries();
                                        let date = null;

                                        for (let pair of headers) {
                                            if (pair[0] === 'date') {
                                                date = new Date(pair[1]);
                                            }
                                        }

                                        if (date) {
                                            let age = parseInt((new Date().getTime() - date.getTime()) / 1000);
                                            let ttl = getTTL(event.request.url);

                                            if (ttl && age > ttl) {

                                                return new Promise(
                                                    (resolve) => {

                                                        return fetch(event.request.clone())
                                                            .then(
                                                                (updatedResponse) => {
                                                                    if (updatedResponse) {
                                                                        cache.put(event.request, updatedResponse.clone());
                                                                        resolve(updatedResponse);
                                                                    } else {
                                                                        resolve(response)
                                                                    }
                                                                }
                                                            )
                                                            .catch(
                                                                () => {
                                                                    resolve(response);
                                                                }
                                                            );

                                                    }
                                                )
                                                    .catch(
                                                        (err) => {
                                                            return response;
                                                        }
                                                    );
                                            } else {
                                                return response;
                                            }

                                        } else {
                                            return response;
                                        }

                                    } else {
                                        return null;
                                    }
                                }
                            )
                            .then(
                                (response) => {
                                    if (response) {
                                        return response;
                                    } else {
                                        return fetch(event.request.clone())
                                            .then(
                                                (response) => {

                                                    if(response.status < 400) {
                                                        if (~SUPPORTED_METHODS.indexOf(event.request.method) && !isBlacklisted(event.request.url)) {
                                                            cache.put(event.request, response.clone());
                                                        }
                                                        return response;
                                                    } else {
                                                        return caches.open(CACHE_VERSIONS.notFound).then((cache) => {
                                                            return cache.match(NOT_FOUND_PAGE);
                                                        })
                                                    }
                                                }
                                            )
                                            .then((response) => {
                                                if(response) {
                                                    return response;
                                                }
                                            })
                                            .catch(
                                                () => {

                                                    return caches.open(CACHE_VERSIONS.offline)
                                                        .then(
                                                            (offlineCache) => {
                                                                return offlineCache.match(OFFLINE_PAGE)
                                                            }
                                                        )

                                                }
                                            );
                                    }
                                }
                            )
                            .catch(
                                (error) => {
                                    console.error('  Error in fetch handler:', error);
                                    throw error;
                                }
                            );
                    }
                )
        );

    }
);


self.addEventListener('message', (event) => {

    if(
        typeof event.data === 'object' &&
        typeof event.data.action === 'string'
    ) {
        switch(event.data.action) {
            case 'cache' :
                precacheUrl(event.data.url);
                break;
            default :
                console.log('Unknown action: ' + event.data.action);
                break;
        }
    }

});
{{< /highlight >}}

## Partial 
Création du partial pour integrer PWA dans Hugo.

*/themes/VOTRETHEME/layouts/partials/pwa.html*

{{< highlight html >}}
<link rel="manifest" href="/manifest.json">

<meta name="mobile-web-app-capable" content="yes" />

<meta name="apple-mobile-web-app-title" content="My PWA" />

<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />

<script>

if ('serviceWorker' in navigator) {

navigator.serviceWorker.register('/sw.js');

};

</script>
{{< /highlight >}}

Et on ajoute a notre *head.html* pour être prit en compte.

{{< highlight html >}}
{{- partial "pwa.html" . -}}
{{< /highlight >}}

## Mots de la fin
J'ai testé sur differents téléphones android et IOS, des fois ca marche bien et d'autre fois à moitié.

{{< pj />}}

## Liens
https://fr.wikipedia.org/wiki/Progressive_web_app

https://jamstatic.fr/2017/03/11/mode-offline-avec-hugo/

https://www.pwabuilder.com/imageGenerator

https://github.com/wildhaber/offline-first-sw

https://discourse.gohugo.io/t/simple-implementation-of-progressive-web-apps-pwa-on-hugo-website/39952


