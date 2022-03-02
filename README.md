# Contexte
Ce projet est réalisé dans le cadre de la formation Microsoft IA et permet de mettre en évidence l'importance du choix des hyperparamètres d'un modèle dans la performance de la prédiction.

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


# Etapes de réalisation du projet

## [x] Création du dataset

## [x] Prétraitement des données
    - [x] Conversion des caractères en miniscule
    - [x] Conversion des coquilles
    - [x] Remplacement des mauvaises données

## [x] Prétraitement du dataset
    - [x] Erreurs de saisie corrigibles
    - [x] Remplacement par des NaN
    - [x] Remplacement des NaN par le mode
    - [x] Recalcul du score
    - [x] Encodage des valeurs catégorielles

## [x] KNN From Scratch
    - [x] Fonction distance
    - [x] Fonction modèle
    - [x] Expérimentation
    - [x] Performances
    - [x] Matrice de confusion
## [x] KNN Sklearn
    - [x] Préparation des données
    - [x] K-fold validation
    - [x] Gridsearch
    - [x] Performances
    - [x] Matrice de confusion

## [x] Comparaison des résultats

## [x] Mise en place de la solution

## [ ] Livrables
    - [x] Un Notebook bien structuré/organisé qui réalise les différentes étapes de ce projet.
    - [x] Un Notebook de l'application adaptée qui affiche les résultats avec et sans IA.
    - [ ] Un Readme.md pour mettre en avant votre projet (exemple : des fonctions à définir, analyse, réalisation ...).
    - [ ] Un compte rendu.
    - [x] Les DataSets et les fichiers nécessaires.