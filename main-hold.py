import pandas as pd

import format
import streamlit as st
import os
from PIL import Image
from vectorize import init_reduce_model  # Si tu l'as dans un fichier 'vectorization.py'


def list_images():
    return sorted(os.listdir("images"))

all_images = list_images()

st.set_page_config(page_title="Archetype", layout="wide")

st.markdown("""
    <style>
        .title {
            font-size: 50px !important;
            color: #f4f6f7 ;
            text-align: center;
            }
    </style>
""", unsafe_allow_html=True)
st.markdown('<p class="title">Archetype Embedding </p>', unsafe_allow_html=True)
arch = st.selectbox("Archetype selectbox", all_images)
col1, col2, col3 = st.columns(3, gap="large", vertical_alignment="top")

with col1:
    st.text_input("Recherche Archetype")
    qqc1 = st.slider("select a number", 0, 5, 0, key="1")
    st.write("qqc1 = ", qqc1)
    qqc4 = st.slider("select a number", 0, 5, 0, key="2")
    st.write("qqc4 = ", qqc4)
    qqc2 = st.slider("select a number", 0, 5, 0, key="3")
    st.write("qqc2 = ", qqc2)
    qqc3 = st.slider("select a number", 0, 5, 0, key="4")
    st.write("qqc3 = ", qqc3)
with col3:
    with st.container(height=450, border=True):
        st.write("Description du Personnage")
        st.write("La Description")
    with st.container(height=450, border=True):
        st.write("Tags du Personnage")
        st.write("Les Tags")



def get_imagepath(arch: str) -> str:
    arch = arch.replace("'", "_")
    arch_dir = os.path.join("images", arch)
    assert os.path.exists(arch_dir)
    for img in os.listdir(arch_dir):
        print(img)
        if img.endswith(".png"):
            return os.path.join(arch_dir, img)
    raise ValueError(f"Image {arch} not found in images ")
chemin_vers_image = get_imagepath(arch)


with col2:
    st.image(chemin_vers_image)

# Champ de texte pour entrer une description
user_input = st.text_input("🔍 Entrez une description d'archétype :", "")

# Vérifier si l'utilisateur a entré du texte
if user_input:
    st.write(f"🔄 Texte entré : {user_input}")  # Debugging

    try:
        # Trouver l'archétype le plus proche
        matched_arch = arch_finder(user_input, vectors_dict, model)

        # Trouver et afficher l'image correspondante
        chemin_vers_image = get_imagepath(matched_arch)

        st.subheader("🖼️ Archétype trouvé :")
        st.image(chemin_vers_image, caption=matched_arch, use_column_width=True)

    except Exception as e:
        st.error(f"🚨 Erreur : {e}")




