from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/retrieve_wikidata/<identifiant>', methods=['GET'])
def retrieve_wikidata(identifiant):
    if identifiant:
        url = f'https://www.wikidata.org/wiki/{identifiant}'

        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            for script in soup(["script", "style"]): 
                script.decompose()

            html = soup.prettify()

            return html
        
        else:
            return "Error"
        
    else:
        return "id non trouvé"

if __name__ == '__main__':
    app.run(debug=True)
