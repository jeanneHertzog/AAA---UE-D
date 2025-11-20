import pandas as pd
import os

fichier_original = "en.openfoodfacts.org.products.tsv"

# Le nom du nouveau fichier échantillon
fichier_allégé = "dataset/products_sample.tsv"

# Nombre de lignes à conserver
N_LIGNES = 9000

try:
    print(f"1. Lecture des {N_LIGNES} premières lignes de : {fichier_original}")

    # Lire le fichier original, en conservant seulement les N_LIGNES
    df_sample = pd.read_csv(
        fichier_original,
        sep='\t',
        nrows=N_LIGNES,
        low_memory=False,
        encoding='utf-8'
    )

    # Création du répertoire 'dataset' s'il n'existe pas
    os.makedirs('dataset', exist_ok=True)

    print(f"2. Sauvegarde dans le nouveau fichier : {fichier_allégé}")

    # Sauvegarder l'échantillon dans un nouveau fichier TSV
    df_sample.to_csv(fichier_allégé, sep='\t', index=False, encoding='utf-8')

    print(f" Fichier allégé créé avec succès. Le fichier contient {len(df_sample)} lignes.")
    print("Vous pouvez maintenant utiliser ce nouveau fichier dans votre notebook.")

except FileNotFoundError:
    print(f"ERREUR : Le fichier original '{fichier_original}' n'a pas été trouvé. Veuillez vérifier le chemin.")
except Exception as e:
    print(f"Une erreur est survenue lors du traitement du fichier : {e}")