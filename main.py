import pandas as pd
import format
import streamlit as st
import os
from PIL import Image
from vectorize import *


def list_images():
    return sorted(os.listdir("images"))



#définition du vector_dict
model,vectors_dict = init_vectorization()
chemin_vers_image_description = None








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

col1, col2 = st.columns(2, gap="large", vertical_alignment="top")



def get_imagepath(arch: str) -> str:
    arch = arch.replace("'", "_")
    arch_dir = os.path.join("images", arch)
    assert os.path.exists(arch_dir)
    for img in os.listdir(arch_dir):
        print(img)
        if img.endswith(".png"):
            return os.path.join(arch_dir, img)
    raise ValueError(f"Image {arch} not found in images ")







with col1:
    arch_selection = st.selectbox("Archetype selectbox", all_images)
    chemin_vers_image_selection = get_imagepath(arch_selection)
    st.image(chemin_vers_image_selection)




with col1:

    with st.container(height=450, border=True):
        st.write("Description du Personnage")
        st.write(get_description(arch_selection))
    with st.container(height=450, border=True):
        st.write("Tags du Personnage")
        st.write(get_tags(arch_selection))










with col2:

    # Champ de texte pour entrer une description
    user_input = st.text_input("🔍 Entrez une description d'archétype :", "")

    # Vérifier si l'utilisateur a entré du texte
    if user_input:
        st.write(f"🔄 Texte entré : {user_input}")  # Debugging

        try:
            # Trouver l'archétype le plus proche
            matched_arch = arch_finder(user_input, vectors_dict, model)

            # Trouver et afficher l'image correspondante
            chemin_vers_image_description = get_imagepath(matched_arch)

            st.subheader("🖼️ Archétype trouvé :")
            st.image(chemin_vers_image_description, caption=matched_arch, use_column_width=True)

        except Exception as e:
            st.error(f"🚨 Erreur : {e}")

with col2:
    if chemin_vers_image_description:
        try:
            with st.container(height=450, border=True):
                st.write("Description du Personnage")
                st.write(get_description(matched_arch))
            with st.container(height=450, border=True):
                st.write("Tags du Personnage")
                st.write(get_tags(matched_arch))
        except Exception as e:
            st.error(f"🚨 Erreur : {e}")


