from flask import Flask, render_template
import pandas as pd
import re
from flask_bootstrap import Bootstrap

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

df = pd.read_csv('auto-ecole-resultats.csv', encoding='ISO-8859-1')
print(df.head()) 

@app.route('/donnees/<int:offset>/<int:length>')
def donnees(offset, length):
    end_index = offset + length

    df['Code_postal'] = df['localité auto école'].apply(postal_code)
    df['Ville'] = df['localité auto école'].apply(ville)
    df['Adresse'] = df['localité auto école'].apply(adresse)
    df['Nom_ecole'] = df['localité auto école'].apply(nom_ecole)

    data = df[offset:end_index]
    print(data)
    
    return render_template('donnees.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
