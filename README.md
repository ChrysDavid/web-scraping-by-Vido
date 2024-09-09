# Web Scraping Project

## Introduction

Ce projet est un script de web scraping développé en Python qui utilise diverses bibliothèques pour extraire des données d'un site web. Il peut être utilisé pour télécharger des images, du texte, et d'autres contenus disponibles sur un site spécifique.

## Aperçu

![Aperçu du projet](src/capture.png)

## Fonctionnalités

- Téléchargement de vidéos YouTube avec la meilleure qualité disponible.
- Téléchargement de playlists YouTube complètes.
- Gestion des fichiers téléchargés dans des dossiers spécifiques.
- Extraction d'informations supplémentaires comme le titre de la vidéo, le nombre de vues, etc.

## Prérequis

Avant d'exécuter ce projet, assurez-vous d'avoir installé les éléments suivants :

- [Python 3.11](https://www.python.org/downloads/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Structure du Projet

    web-scraping-by-Vido/
    │
    ├── main.py               # Script principal pour exécuter le téléchargement
    ├── youtube_downloader.py # Module contenant les fonctions de téléchargement
    ├── README.md             # Documentation du projet
    └── venv/                 # (Facultatif) Environnement virtuel Python


## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/ChrysDavid/web-scraping-by-Vido.git
   cd web-scraping-by-Vido


2. Activez l'environnement virtuel :
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Sur Windows
    source venv/bin/activate  # Sur macOS/Linux


3. Exécutez le script :
    ```bash
    python main.py

