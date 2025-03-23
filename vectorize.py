from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import config

_vectorizer = SentenceTransformer(config.VECTORIZER)

def make_text(data: dict)->str:
    """
    on par du principe que les colones sont 'category', 'description_en', 'tags_fr', 'description_fr', 'color',
       'sub_category', 'values'
    :param data: c'est la donnée d'un personnage
    :return: renvoie le texte qui se fera vectoriser
    """
    output = data["description_fr"] + " tags: " +data["tags_fr"]
    return output


def make_vector(text : str)-> np.array: #array : liste mais plus efficace pour vectoriser
    """
    permet de vectoriser le text
    :param text: la description et le tags du personnage (l'output de la fonction make_text)
    :return: la vectorisation des descriptions
    """
    vector = _vectorizer.encode(text)
    return vector










if __name__ == '__main__':
    df = pd.read_json("data_format.json").T #.T inverse les lignes et les colones
    for arch in df.index :
        out = make_text(df.loc[arch])
        print(out)
        exit()
    #print(df.head())
    #print(df.columns)