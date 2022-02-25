# Fonctions pour étude de faisabilité moteur de classification
# Fonction pour calcul PCA

# Importation librairies
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import plotly.graph_objects as go
import matplotlib
import seaborn as sns
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer, InterclusterDistance


def calcul_pca(image_features, n_component, method_std):

    print("Dimensions dataset avant réduction PCA : ", image_features.shape)

    if method_std == None:
        # Pipeline de pre-processing sans standardisation
        pca = Pipeline([("pca", PCA(n_components=n_component))])
        
    else:
    # Pipeline de pre-processing avec standardisation
        pca = Pipeline([("preprocessor", method_std),
                        ("pca", PCA(n_components=n_component))])
                        
    feat_pca = pca.fit_transform(image_features)

    print("Dimensions dataset après réduction PCA : ", feat_pca.shape)

    return feat_pca

# Fonction pour calcul classification T-SNE


def classif_tsne(features, nb_comp):

    # Instantiation du T-SNE
    tsne = TSNE(n_components=nb_comp,
                perplexity=30,
                n_iter=300,
                n_jobs=-1,
                #init='pca',
                verbose=1
                )

    # Application du T-SNE
    X_projected = tsne.fit_transform(features)

    return X_projected

# Fonction pour la représentation graphique des points par T-SNE


def proj_grade_tsne(tsne_proj, nbre_color, col):

    # Affichage des points en 2D
    plt.figure(figsize=(8, 8))

    # Definition du titre
    plt.title("Visualisation t-SNE 2D\n")

    plot = sns.scatterplot(
        x="tsne-2d-axe 1", y="tsne-2d-axe 2",
        hue=tsne_proj[col].tolist(),
        palette=sns.color_palette("hls", nbre_color),
        data=tsne_proj,
        legend="full",
        s=10,
        alpha=0.7)

    # Modification taille de la légende
    plt.setp(plot.get_legend().get_texts(), fontsize='8')

    plt.show()

    return None

# Fonction pour la représentation graphique 3D des points par T-SNE (mode interactif)


def proj_grade_tsne_3d_interactif(tsne_proj, col):

    fig = go.Figure()

    col_types = tsne_proj[col].unique().tolist()

    # Affichage du graphe 3D selon les colonnes du dataframe
    for col_name in col_types:
        val = tsne_proj[col] == col_name
        fig.add_trace(go.Scatter3d(x=tsne_proj['tsne-3d-axe 1'][val],
                                   y=tsne_proj['tsne-3d-axe 2'][val],
                                   z=tsne_proj['tsne-3d-axe 3'][val],
                                   name=col_name,
                                   mode="markers",
                                   ))

    # Modification de la taille et de l'opacité des marqueurs
    fig.update_traces(marker=dict(size=1.5,
                                  opacity=0.7))

    # Modification de la taille de la figure
    fig.update_layout(
        width=800,
        height=800,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        ))

    # Ajout des labels des axes et de la légende
    fig.update_layout(
        scene=dict(xaxis_title='tsne-3d-axe 1',
                   yaxis_title='tsne-3d-axe 2',
                   zaxis_title='tsne-3d-axe 3'),
        legend_title_text='Catégories')

    # Redimensionnement de la légende
    fig.update_layout(legend={'itemsizing': 'constant'})

    fig.show()

    return None

# Fonction k-means pour calcul k-means


def calcul_kmeans(df_in, nbre_clusters):
    model_kmeans = KMeans(init='k-means++', n_clusters=nbre_clusters)
    cluster_kmeans = model_kmeans.fit(df_in)

    return model_kmeans, model_kmeans.labels_

# Fonction pour le calcul du coefficient de silhouette pour un k-means avec un nombre de clusters donné


def calcul_coef_silhouette_kmeans(df_in, clusterer):
    visualizer = SilhouetteVisualizer(clusterer)
    visualizer.fit(df_in)
    visualizer.show()

    return None
