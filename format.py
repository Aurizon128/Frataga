import pandas as pd
from vectorize import make_text, make_vector
import config


def vectorize_data(input_path : str)-> None:
    """
    permet de stocker les vectorisations
    :param input_path: le chemin vers le json
    :return: None
    """
    df : pd.DataFrame = pd.read_json(input_path).T
    df["Vector:" + config.VECTORIZER] = None # Gpt
    for arch in df.index :
        data = df.loc[arch]
        vector = make_vector(make_text(data=data))
        df.at[arch, "Vector:"+config.VECTORIZER] = vector
    df.T.to_json(input_path, indent=4, force_ascii=False)







def format_xlsx(input_path:str,output_path:str) -> None:
    """
    la fonction crée un un fichier nommer dataformat avec toutes les informations du xlsx formaté
    :param input_path: le fichier xlsx
    :param output_path: le chemin vers le fichier de sortie
    :return: None
    """
    df : pd.DataFrame = pd.read_excel(input_path)
    df["name"]=df["name"].apply(lambda x: x.strip()) #retire les espaces
    df = df.set_index("name")
    df = df.drop(columns=["Tags","Lien image"])
    for arch in df.index :

        #Format des catégories
        data = df.loc[arch]
        category = data["category"]
        c1,c2=category.split("/")
        c1=c1.strip().lower()
        c2=c2.strip().lower()
        df.at[arch, "category"] = c1
        df.at[arch, "sub_category"] = c2

        #Format des descriptions
        data = df.loc[arch]
        description_fr = data["description_fr"]
        parts = description_fr.split(":")
        name,desc,values=parts

        desc = desc.removesuffix("Valeurs ")
        df.at[arch, "description_fr"] = desc
        df.at[arch, "values"] = values
    df.T.to_json(output_path, indent=4,force_ascii=False)


if __name__ == '__main__':
    format_xlsx(input_path="archetypes_translated ultimate.xlsx", output_path="data_format.json")
    vectorize_data(input_path="data_format.json")