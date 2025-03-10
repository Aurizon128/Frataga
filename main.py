from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from archetypes import Archetype, load, all_archetypes
import numpy as np


archs= all_archetypes()

descriptions = {}
for arch in archs:
    descriptions[arch.nom] = arch.description + " " + ", ".join(arch.tags)

documents = []
cles = []
for key, val in descriptions.items():
    documents.append(val)
    cles.append(key)

model = SentenceTransformer('Sahajtomar/french_semantic')
#model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# Transformer les textes en vecteurs
doc_embeddings = model.encode(documents)
query = input("Entrez votre query:")
query_embedding = model.encode([query])

# Calcul de similarité cosinus
scores = cosine_similarity(query_embedding, doc_embeddings)[0]
print(scores)
id_meilleur_score = np.argmax(scores)
meilleur_archetype = cles[id_meilleur_score]
print(f"Le meilleur archetype est {meilleur_archetype} avec un score de {max(scores)}")