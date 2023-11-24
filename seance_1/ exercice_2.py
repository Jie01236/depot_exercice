import os

chemin_courant = os.getcwd()
print("chemin du dossier courant:" + chemin_courant)

nom_dir_courant = os.path.basename(chemin_courant)
print("nom du répertoire courant:" + nom_dir_courant)

nouveau_nom_rep= "nouveau_repertoire"
os.makedirs(nouveau_nom_rep)
print("Créer un répertoire :" + nouveau_nom_rep)

os.rmdir(nouveau_nom_rep)
print("Supprimer le répertoire:" + nouveau_nom_rep)

lister = os.listdir(chemin_courant)
print("Lister les fichiers et les dossiers:" + str(lister))