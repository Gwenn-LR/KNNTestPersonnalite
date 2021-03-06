# Contexte
Ce projet est réalisé dans le cadre de la formation Microsoft IA et permet de mettre en évidence l'importance du choix des hyperparamètres d'un modèle dans la performance de la prédiction.

Cette étude est appliquée à l'étude des techniques de classification supervisée, plus particulièrement le classificateur KNN (K plus proches voisins) implémenté en python.

Il est composé de :
- Run_Questionnaire : le dossier contenant les fichiers nécessaire à l'exécution du questionnaire
    - DataSet : le dossier contenant les fichiers .csv des réponses au questionnaire
    - ConcatenationDataset.py : le script permettant de générer un fichier .csv de toutes les réponses
    - DataSetTotal.csv : le fichier .csv récapitulant toutes les réponses
    - Run.ipynb : le fichier jupyter permettant de répondre au questionnaire
    - Test.py : le script permettant de généré le questionnaire
- KNN - Test de personnalité.ipynb : le fichier permettant de générer un modèle prédictif à partir des fichiers
- ModeleKNN.pkl : le fichier du modèle sérialisé, généré par joblib
- README.md : ce fichier


# Détails de l'application

Il est composé de :
- Run_Questionnaire : le dossier contenant les fichiers nécessaire à l'exécution du questionnaire
    - DataSet : le dossier contenant les fichiers .csv des réponses au questionnaire
    - ConcatenationDataset.py : le script permettant de générer un fichier .csv de toutes les réponses
    - DataSetTotal.csv : le fichier .csv récapitulant toutes les réponses
    - Run.ipynb : le fichier jupyter permettant de répondre au questionnaire
    - Test.py : le script permettant de généré le questionnaire
    
    
- .gitignore : le fichier git permettant d'ignorer des fichiers de l'espace de travail


- Compte rendu.ipynb : le fichier compte rendu du brief
    
    
- KNN - Test de personnalité.ipynb : le fichier permettant de générer un modèle prédictif à partir des fichiers


- ModeleKNN.pkl : le fichier du modèle sérialisé, généré par joblib


- README.md : ce fichier


# Etapes de réalisation du projet

## [x] Création du dataset
    - [x] Réponses au questionnaire
    - [x] Concatenation des réponses

## [x] Prétraitement des données
    - [x] Récupération des données
    - [x] Conversion des caractères en minuscule
    - [x] Conversion des coquilles
    - [x] Remplacement des NaN par le mode
    - [x] Recalcul du Score
    - [x] Encodage des valeurs catégorielles
    - [x] Séparation des données

## [x] KNN From Scratch
    - [x] Fonction distance
    - [x] Fonction modèle
    - [x] Expérimentation
        - [x] Distance euclidienne
        - [x] Distance manhattan
        - [x] Distance minkowski
    - [x] Performances
    - [x] Matrice de confusion
## [x] KNN Sklearn
    - [x] Importation de la classe KNeighborsClassifier
    - [x] Préparation des données
    - [x] K-fold validation
    - [x] Gridsearch
    - [x] Performances
    - [x] Matrice de confusion

## [x] Comparaison des résultats

## [x] Mise en place de la solution

## [x] Livrables
    - [x] Un Notebook bien structuré/organisé qui réalise les différentes étapes de ce projet.
    - [x] Un Notebook de l'application adaptée qui affiche les résultats avec et sans IA.
    - [x] Un Readme.md pour mettre en avant votre projet (exemple : des fonctions à définir, analyse, réalisation ...).
    - [x] Un compte rendu.
    - [x] Les DataSets et les fichiers nécessaires.