from flask import Flask, render_template
import pandas as pd
import re
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)

def postal_code(libelle):
    match = re.search(r'\b\d{5}\b', libelle)
    if match:
        return match.group()
    return None

def ville(libelle):
    match = re.search(r'\b\d{5}\b', libelle)
    if match:
        apres_code_postal = match.end()
        ville = libelle[apres_code_postal:].strip()
        return ville
    return None

def adresse(libelle):
    match1 = re.search(r'\b\d{1,3}\b', libelle)
    match2 = re.search(r'\b\d{5}\b', libelle)
    if match1 and match2:
        address = libelle[match1.start():match2.start()].strip()
        return address
    return None

def nom_ecole(libelle):
    match = re.search(r'\b\d{1,3}\b', libelle)
    if match:
        nom_ecole = libelle[:match.start()].strip()
        return nom_ecole
    return None

@app.route('/donnees/<int:offset>/<int:length>')
def donnees(offset=0, length=10):
    df = pd.read_csv("https://www.data.gouv.fr/storage/f/2014-05-06T19-39-42/auto-ecole-resultats.csv", 
        encoding = "ISO-8859-1",  
        sep = ",",
        header = 0)
      
    df.drop(df.columns[[1, 2, 5]], axis=1, inplace = True)

    df['Code_postal'] = df['localité auto école'].apply(postal_code)
    df['Ville'] = df['localité auto école'].apply(ville)
    df['Adresse'] = df['localité auto école'].apply(adresse)
    df['Nom_ecole'] = df['localité auto école'].apply(nom_ecole)
    
    total = len(df)
   # 计算结束索引
    end_index = offset + length

    # 使用 iloc 进行分页
    donnees = json.loads(df.iloc[offset:end_index].to_json(orient="records"))
    
    return render_template('donnees.html', data=donnees, offset=offset, length=length, total=total)
    

if __name__ == '__main__':
    app.run(debug=True)