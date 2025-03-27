import pandas as pd
import format
import streamlit as st
import os
from PIL import Image, ImageDraw
from vectorize import *
from Pylette import extract_colors, Color

def list_images():
    return sorted(os.listdir("images"))



#définition du vector_dict
model,vectors_dict = init_vectorization()
all_images = list_images()

def find_color_palette(img_path) ->list[Color]:
    return [extract_colors(image=img_path, palette_size=8)[i].rgb for i in range(8)]

def get_palette(colors, padding=5):
    """
    Save a color palette as a PNG image.

    Parameters:
        colors (list of array-like): List of RGB colors (e.g., [array([R,G,B]), ...])

        padding (int): Padding between color blocks.
    """
    width = 1024
    cell_width = int((width - padding) / len(colors) - padding)
    cell_height = 128
    height = cell_height + 2 * padding

    img = Image.new("RGB", (width, height + 2*padding), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    for i, color in enumerate(colors):
        x0 = padding + i*(cell_width + padding)
        y0 = padding
        x1 = x0 + cell_width
        y1 = y0 + cell_height
        draw.rectangle([x0, y0, x1, y1], fill=tuple(color))
    return img


def get_imagepath(arch: str) -> str:
    arch = arch.replace("'", "_")
    arch_dir = os.path.join("images", arch)
    assert os.path.exists(arch_dir)
    for img in os.listdir(arch_dir):
        if img.endswith(".png"):
            return os.path.join(arch_dir, img)
    raise ValueError(f"Image {arch} not found in images ")


def afficher_par_selection():
    arch_selection = st.selectbox("Selection de l'archetype", all_images)
    chemin_vers_image_selection = get_imagepath(arch_selection)
    st.image(chemin_vers_image_selection)
    col1, col2 = st.columns(2)
    with col1:
        st.write("Description du Personnage")
        st.write(get_description(arch_selection))
    with col2:
        st.write("Tags du Personnage")
        st.write(get_tags(arch_selection))
    st.image(get_palette(find_color_palette(chemin_vers_image_selection)))



def afficher_par_description():
    # Champ de texte pour entrer une description
    user_input = st.text_input("Entrez une description d'archétype  :",placeholder="J'aime la nature et la musique")

    # Vérifier si l'utilisateur a entré du texte

    if user_input:
        # Trouver l'archétype le plus proche
        matched_arch = arch_finder(user_input, vectors_dict, model)
        # Trouver et afficher l'image correspondante
        chemin_vers_image_description = get_imagepath(matched_arch)
        st.subheader(matched_arch)
        st.image(chemin_vers_image_description, use_container_width=True)

        if chemin_vers_image_description:
            col1, col2 = st.columns(2)
            with col1:
                st.write("Description du Personnage")
                st.write(get_description(matched_arch))
            with col2:
                st.write("Tags du Personnage")
                st.write(get_tags(matched_arch))
            st.image(get_palette(find_color_palette(chemin_vers_image_description)))





if __name__ == '__main__':
    st.set_page_config(page_title="Archetype")

    st.markdown("""
        <style>
            .title {
                font-size: 50px !important;
                color: #f4f6f7 ;
                text-align: center;
                }
        </style>
    """, unsafe_allow_html=True)
    # st.markdown('<p class="title">Archetype Embedding </p>', unsafe_allow_html=True)
    st.title("MythiCanvas")
    # col1, col2 = st.columns(2, gap="large", vertical_alignment="top")
    # with col1:
    #     afficher_par_description()
    # with col2:
    #     afficher_par_selection()

    tab_description,tab_selection = st.tabs(["description","selection"])
    with tab_description:
        afficher_par_description()
    with tab_selection:
        afficher_par_selection()


