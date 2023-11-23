import os

chemin_courant = os.getcwd()
print("chemin du dossier courant:" + chemin_courant)

nom_dir_courant = os.path.basename(chemin_courant)
print("nom du répertoire courant:" + nom_dir_courant)

nouveau_nom_dir= "new_directory"
os.makedirs(nouveau_nom_dir)
print("Créer un répertoire :" + nouveau_nom_dir)

os.rmdir(nouveau_nom_dir)
print("Supprimer le répertoire:" + nouveau_nom_dir)

# 列出当前目录中的文件和文件夹
lister = os.listdir(chemin_courant)
print("Lister les fichiers et les dossiers" + str(lister))