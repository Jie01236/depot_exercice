from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

json_file = 'data.json'

@app.route('/parcs_eoliens')
def parcs_eoliens():
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file) 

    return render_template('parcs_eoliens.html', data=data)

@app.route('/parcs_eoliens/<identifiant>')
def info(identifiant):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file) 
    
    info = None
    for item in data:
        if item['recordid'] == identifiant:
            info = item
            break

    if info:
        return render_template('info.html', info=info)
    else:
        return "Identifiant non trouvé"

if __name__ == '__main__':
    app.run(debug=True)
