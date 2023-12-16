from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

json_file = 'data.json'

@app.route('/parcs_eoliens')
def parcs_eoliens():
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file) 

    return render_template('parcs_eoliens.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
