from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/pays")
def pays():
    data = [{"nom":"France",
            "capital":"Paris",
            "continent":"Europe"},
        {"nom":"Etats-Unis",
            "capital":"Washington",
            "continent":"Europe"},
        {"nom":"Egypte",
            "capital":"Le Caire",
            "continent":"Afrique"},
        {"nom":"Chine",
            "capital":"Pekin",
            "continent":"Asie"}]
    return render_template("pays.html", pays=data)

if __name__ == '__main__':
    app.run(debug=True)