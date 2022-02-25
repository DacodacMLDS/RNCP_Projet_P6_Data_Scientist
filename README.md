<h1>Projet 6: Classifiez automatiquement des biens de consommation</h1>
  
![My Image](marketplace.jpg)

<h2>Contexte et problématique du projet</h2>

Vous êtes Data Scientist au sein de l’entreprise "Place de marché”, qui souhaite lancer une marketplace e-commerce.

Sur la place de marché, des vendeurs proposent des articles à des acheteurs en postant une photo et une description.

Pour l'instant, l'attribution de la catégorie d'un article est effectuée manuellement par les vendeurs et est donc peu fiable. De plus, le volume des articles est pour l’instant très petit.

Pour rendre l’expérience utilisateur des vendeurs (faciliter la mise en ligne de nouveaux articles) et des acheteurs (faciliter la recherche de produits) la plus fluide possible et dans l'optique d'un passage à l'échelle, il devient nécessaire d'automatiser cette tâche.

Linda, lead data scientist, vous demande donc d'étudier la faisabilité d'un moteur de classification des articles en différentes catégories, avec un niveau de précision suffisant.

<h2>But et intérêt du projet</h2>

Réalisation d'une première étude de faisabilité d'un moteur de classification d'articles basé sur une image et une description pour l'automatisation de l'attribution de la catégorie de l'article, à partir des données suivante : https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Textimage+DAS+V2/Dataset+projet+pre%CC%81traitement+textes+images.zip

- Analyse des données
- Pré-traitement des descriptions de produit (approche NLP) et des images (SIFT, réseaux de neurones à convolution CNN VGG16 ResNet50)
- Réduction de dimensions PCA
- Clustering
- Les résultats du clustering sont présentés sous la forme d’une représentation en deux dimensions à déterminer, qui illustrera le fait que les caractéristiques extraites permettent de regrouper des produits de même catégorie (TSNE 2D et 3D).

<h2>Compétences évaluées</h2>

- Représenter graphiquement des données à grandes dimensions
- Mettre en œuvre des techniques de réduction de dimension
- Prétraiter des données texte pour obtenir un jeu de données exploitable
- Prétraiter des données image pour obtenir un jeu de données exploitable

<h2>Contenu du dépôt GitHub</h2>

- README.md: fichier présentation projet

- marketplace.jpg : image illustration README.md

- Répertoire "Notebooks":
  - fichier "functions_p6_project.py": fichier pour fonctions externes en Python
  - fichier "P6_01_notebook.ipynb": fichier notebook Jupyter en Python pour le pré-traitement des données, la réduction de dimensions, le clustering et la représentation graphique des données
  
- Répertoire "Soutenance":
  - fichier "P6_02_support_soutenance_ppt.ppt": fichier support soutenance projet Powerpoint
  - fichier "P6_03_support_soutenance_pdf.pdf": fichier support soutenance projet PDF
  - fichier "projet_p6_oc_ds.mp4": video soutenance projet P6 (mp4)
  - fichier "Projet 6 valide - Classifiez automatiquement des biens de consommation - OC.pdf": preuve de validation du projet P6
