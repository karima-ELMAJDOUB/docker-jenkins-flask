# Projet MLOps avec Dataset Iris

Ce projet démontre la mise en œuvre d'un pipeline MLOps pour un modèle basé sur le dataset Iris. Le déploiement est réalisé à l'aide de ngrok, Jenkins, Docker et GitHub.

## Contenu du Projet

- **`model.py`**: Script Python pour l'entraînement d'un modèle de classification sur le dataset Iris.
- **`request.py`**: Script pour tester le modèle avec une requête d'échantillon.
- **`server.py`**: Application Flask pour le déploiement du modèle.
- **`Dockerfile`**: Fichier pour la construction de l'image Docker encapsulant l'environnement d'exécution.
- **`requirements.txt`**: Liste des dépendances Python nécessaires pour exécuter l'application.

## Dataset Iris

Le modèle est entraîné sur le célèbre dataset Iris, comprenant des exemples de trois espèces de fleurs. Les labels sont : Setosa, Versicolor, Virginica.

## Entraînement du Modèle

Le modèle est un classificateur d'arbre de décision, entraîné avec scikit-learn.

## Déploiement avec jenkins

Le déploiement continu du modèle est automatisé à l'aide de Jenkins. Le pipeline Jenkins est configuré pour intégrer les étapes d'entraînement du modèle, de tests et de déploiement.




