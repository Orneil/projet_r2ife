
    # ... Reste de votre code Streamlit ...


# Importer les bibliothèques nécessaires
import streamlit as st
import pandas as pd
import base64
import urllib.request
import shutil
import os
import zipfile
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

if __name__ == "__main__":
    st.set_page_config(layout="wide")


# ####################### IMPORTATION DES FICHIERS: Modifier chemin du fichier Excel ####################################################################

# Chargement du fichier Excel depuis Google Drive (via le lien de partage)
google_drive_link = "https://docs.google.com/spreadsheets/d/1GgMH4_rNkMNAl-4FBpmbgWwvGVbE_1p2/edit?usp=drive_link"

# Extraction de l'ID du fichier depuis le lien
file_id = google_drive_link.split('/')[-2]

# Construction du lien de téléchargement direct
download_link = f'https://drive.google.com/uc?id={file_id}'

excel_file = pd.ExcelFile(download_link)

# Lire le fichier Excel avec l'option sheet_name pour spécifier la feuille
df_raw = pd.read_excel(excel_file)

# Création du DataFrame
df_raw = pd.DataFrame(df_raw)
df = df_raw.copy()


column_order = ["Nom", "Prenoms", "Niveau", "Formation", "Etablissement","Email", "Telephone", "Competences","CV"]
df = df[column_order]


# ########################## ENTETE #######################################################################################

# Ajout du logo, position au niveau de barre à gauche
logo_url = f'https://drive.google.com/file/d/1KHwPzRS3ezd483wNta5KIvhQGZULrC1s/view?usp=drive_link'
st.image("LOGOS.png", width=500, output_format = "PNG")
# st.image(logo_url, width=100, output_format = "PNG")

st.title(":orange[Base de données pour recrutement]")
st.write(
  """

  """
)
st.write("""Le Réseau des Ingénieurs Ivoiriens Formés à l'Etranger regroupe un grand nombre de talents de la diaspora qui apporteront beaucoup à vos entreprises. Grâce à cet outil, vous pouvez accéder aux différents CVs et prendre contact avec les profils qui vous intéressent.""" )

st.write(
  """

  """
)

st.markdown('### :pushpin: Données sur les profils Ingénieurs')





######################### AUTHENTIFICATION #############################################################################


names = ['Yao Gnabeli', 'Rebecca Briggs']
usernames = ['gyao', 'rbriggs']
passwords = ['r2ifegyao', '456']
hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
authenticator.cookie_expiry_days = 30

# ##########################authenticator = stauth.Authenticate(names, usernames, hashed_passwords,'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)#######################################################################################
name, authentication_status, username = authenticator.login('Connexion', 'sidebar')



if authentication_status:
    authenticator.logout('Déconnexion', 'sidebar')
    st.sidebar.write(f'Bienvenue *{name}*')
    ############ Ajout Noellie  FILTRES #########################################################################
    # Liste des modalités de la colonne à filtrer
    all_formations = df['Formation'].unique()
    all_etablissement = df['Etablissement'].unique()
    all_niveau = df['Niveau'].unique()

    # Sélection de la modalité via une liste déroulante

    col1,col2,col3 = st.columns(3)

    with col1:
        selected_formation = st.selectbox("Domaine de formation", [""] + list(all_formations), index=None, placeholder="Choisir une option")

    with col2:
        selected_etablissement = st.selectbox("Etablissement", [""] + list(all_etablissement), index=None, placeholder="Choisir une option")

    with col3:
        selected_niveau = st.selectbox("Niveau d'étude", [""] + list(all_niveau), index=None, placeholder="Choisir une option")


    if selected_formation or selected_etablissement or selected_niveau:
        condition_formation = df['Formation'] == selected_formation if selected_formation else True
        condition_etablissement = df['Etablissement'] == selected_etablissement if selected_etablissement else True
        condition_niveau = df['Niveau'] == selected_niveau if selected_niveau else True
        df_filtre = df[condition_formation & condition_etablissement & condition_niveau ]
        st.write("Données filtrées :")
        st.data_editor(
            df_filtre,
            column_config={"CV": st.column_config.LinkColumn("Lien vers le CV",display_text="Ouvrir le lien",disabled = True),
            "Nom": st.column_config.Column(disabled = True),
            "Prenoms": st.column_config.Column(disabled = True),
            "Niveau": st.column_config.Column(disabled = True),
            "Formation": st.column_config.Column(disabled = True),
            "Etablissement": st.column_config.Column(disabled = True),
            "Email": st.column_config.Column(disabled = True),
            "Telephone": st.column_config.Column(disabled = True),
            "Competences": st.column_config.Column(disabled = True)},hide_index=True)
    else:
        st.data_editor(
            df,
            column_config={"CV": st.column_config.LinkColumn("Lien vers le CV",display_text="Ouvrir le lien",disabled = True),
            "Nom": st.column_config.Column(disabled = True),
            "Prenoms": st.column_config.Column(disabled = True),
            "Niveau": st.column_config.Column(disabled = True),
            "Formation": st.column_config.Column(disabled = True),
            "Etablissement": st.column_config.Column(disabled = True),
            "Email": st.column_config.Column(disabled = True),
            "Telephone": st.column_config.Column(disabled = True),
            "Competences": st.column_config.Column(disabled = True)},hide_index=True)

    st.markdown("_Dernière mise à jour : Novembre 2023_")



elif authentication_status == False:
    st.sidebar.error('Username/password est incorrect')
elif authentication_status == None:
    st.sidebar.warning("Entrez votre Nom d'utilisateur et votre mot de passe pour accéder aux données")

st.sidebar.write(
  """





  """
)
st.sidebar.write(
  """
  Plus d'infos sur nous:

  :link: www.r2ife-inge.com"""
)
st.sidebar.write(
  """Contacts :

  :e-mail: r2ife.reseau@gmail.com

  :telephone_receiver: +33 767389260 (Murielle Yao)

  :telephone_receiver: +225 09200191 (Kemi Ilupeju)"""
)


