# ###################### A MODIFIER:SUPPRIMER: pour affichage dans un tunnel local ######################################
# Installer de nvm (Node Version Manager)
!curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# Sourcer le fichier de configuration de nvm pour rendre la commande nvm disponible
!source ~/.nvm/nvm.sh

# Installer Node.js v14.16.0
!nvm install v14.16.0

# Activer la version installée
!nvm use v14.16.0
!pip install pyngrok --upgrade -q

# installer le tunel ouvrir le site en local
!npm install -g localtunnel -q
!wget -q -O - ipv4.icanhazip.com

# ############ BIB INDISPENSABLES ##################################################
!pip install streamlit -q
!pip install streamlit-authenticator==0.1.5


# ########### A SUPPRIMER: pour affichage dans un tunnel local , remplacer par la commande suivante#########""""
!streamlit run app.py & npx localtunnel --port 8501

# !streamlit run --browser.gatherUsageStats=False app.py   # A décommenter
