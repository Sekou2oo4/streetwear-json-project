Projet Streetwear JSON API - Digital Ecosystem (DES)

Présentation du projet

Dans le cadre de notre cours Digital Ecosystem (DES), nous avons réalisé un projet qui consiste à créer une API JSON personnalisée hébergée sur GitHub Pages, puis à développer un script Python capable de récupérer et d’afficher ces données.

Nous avons choisi comme thème une marque de streetwear, qui nous permet d’aborder des notions liées à la gestion de données, l’utilisation d’API, et l’hébergement web statique via GitHub Pages.

Le but était d’appliquer les compétences vues en classe pour manipuler des données JSON et utiliser Python pour interagir avec des APIs externes.

Description du projet

Nous avons créé un fichier JSON (streetwear_data.json) contenant plusieurs objets représentant différents articles de la marque de streetwear. Chaque objet contient :

name : le nom de l’article (exemple : "Sneakers X")
description : une courte description de l’article 
specifications : un objet avec des détails techniques (couleur, taille, …)
tags : un tableau de mots-clés liés à l’article (exemple : ["chaussures", "urbain", "confort"])
Ces données sont ensuite hébergées publiquement sur GitHub Pages pour être accessibles via une URL.

Fonctionnement du script Python

Le script fetch_data.py utilise la bibliothèque Python requests pour récupérer les données JSON directement depuis l’URL GitHub Pages.

Une fois les données téléchargées, le script les parse (les transforme en objets Python) puis affiche dans la console les informations clés de chaque article : nom, description, spécifications, et tags.

Le script contient aussi une gestion d’erreurs simple pour afficher un message clair si la récupération des données échoue (problème réseau, URL incorrecte…).

Installation et utilisation

Pour utiliser ce projet, voici les étapes à suivre :

Cloner le dépôt
Ouvrez un terminal et tapez :
git clone https://github.com/Sekou2oo4/streetwear-json-project.git
Installer la bibliothèque requests
Si elle n’est pas déjà installée sur votre machine, lancez :
pip install requests
Lancer le script Python
Positionnez-vous dans le dossier du projet et exécutez :
cd streetwear-json-project
python3 fetch_data.py
Vous verrez alors dans la console les informations de chaque article streetwear s’afficher clairement.

Organisation des fichiers

Voici la structure de notre projet :

streetwear-json-project/
│
├── fetch_data.py           # Script Python qui récupère et affiche les données JSON
├── streetwear_data.json    # Fichier JSON contenant nos données d’articles streetwear
├── README.md               # Documentation du projet
Hébergement et accès aux données JSON

Le fichier streetwear_data.json est hébergé sur GitHub Pages, ce qui permet d’y accéder via une URL publique :

https://sekou2oo4.github.io/streetwear-json-project/streetwear_data.json

Cette URL est utilisée par le script Python pour récupérer les données.

Difficultés rencontrées et solutions


Gestion des erreurs dans Python : Il a fallu ajouter des blocs try/except pour gérer les cas où la connexion à l’URL pourrait échouer.
Hébergement sur GitHub Pages : Nous avons découvert comment activer GitHub Pages pour rendre notre JSON accessible publiquement.
Ces étapes ont renforcé notre compréhension pratique des outils collaboratifs et du développement web.

Membres du groupe

Sekou Doucoure
Dikra
Joelle
