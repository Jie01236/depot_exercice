from ..app import app, db
from flask import render_template
from ..models.factbook import Country, Map, Resources
from sqlalchemy import or_
from sqlalchemy import distinct
#---------------------------------------------- CORRECTION  3 et 5 -------------------------------------------------------------------------
@app.route("/pays")
@app.route("/pays/<int:page>")
def pays(page=1):
    return render_template("pages/pays.html", 
        sous_titre="Pays", 
        donnees= Country.query.order_by(Country.name).paginate(page=page, per_page=app.config["PAYS_PER_PAGE"]))

#确保有一个名为un_pays的路由在您的Flask应用中定义，并且这个路由接受一个参数nom_pays
#否则En tentant de cliquer sur le lien http://localhost:5000/continents/Africa, 
#il y a une erreur « werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'un_pays' with values ['nom_pays']. Did you mean 'tous_pays' instead? » 
#la route manque en effet dans generales.py
@app.route("/pays/<string:nom_pays>")
def un_pays(nom_pays):
    return render_template("pages/un_pays.html", 
        sous_titre=nom_pays, 
        donnees= Country.query.filter(Country.name == nom_pays).first())

#---------------------------------------------- EXERCICE 3 et 5 -------------------------------------------------------------------------

#exercice_3 pour seance_4(/continents:)
#exercicei_5 pour seance_4(/continents:)
@app.route("/continents")
@app.route("/continents/<int:page>")
def continents(page=1):
    # on va créer un dictionnaire (JSON) avec en clé les continents et en valeur une liste de pays
    # il faut initialiser ce dictionnaire au début 
    # correction de TD_5
    pays_par_continent = {}
    # ajouter un dictionnaire dans la route au lieu d'utiliser |length dans html
    pays_count_par_continent = {}  # ajouter des nombre de pays

    for pays in Country.query.all():
        for continent in pays.maps:
            # si la clé (continent) existe déjà dans le dictionnaire, alors il est simplement nécessaire 
            # d'ajouter le pays s'il n'est pas déjà présent
#--- CORRECTION -----------------------------------------------------------------------------------
            if continent.name in pays_par_continent:
            #Effectuer directement « if pays.name not in pays_par_continent[continent.name] » ne peut pas fonctionner 
            #lors de la première itération sur chaque continent : Il faur verifier la présence de continent.name dans le dictionnaire
                if pays.name not in pays_par_continent[continent.name]:
                    pays_par_continent[continent.name].append(pays.name)
                    pays_count_par_continent[continent.name] = pays_count_par_continent.get(continent.name, 0) + 1
                # sinon il faut créer la clé et initialiser la valeur
            else:
                pays_par_continent[continent.name] = [pays.name]
                pays_count_par_continent[continent.name] = 1

    return render_template("pages/continents.html",
        sous_titre="Continents",
        donnees=Map.query.paginate(page=page, per_page=app.config["PAYS_PER_PAGE"]),
        donnees_generales=pays_par_continent,
        pays_count=pays_count_par_continent) #ajouter un variable 

#exercice_3 pour seance_4(/continents/<nom_continent>)
#correction TD_5
@app.route("/continents/<string:nom_continent>")
def un_continent(nom_continent):
    continent = Map.query.filter(Map.name == nom_continent).first()

    return render_template("pages/un_continent.html", 
        sous_titre=nom_continent, 
        donnees= Country.query.filter(Country.maps.contains(continent)).order_by(Country.name).all())

#exercice_3 pour seance_4(/ressources)
#exercice_5 pour seance_4(/ressources)
@app.route("/ressources")
@app.route("/ressources/<int:page>")
def ressources(page=1):
    # on va créer un dictionnaire (JSON) avec en clé les continents et en valeur une liste de pays
    # il faut initialiser ce dictionnaire au début 
    pays_par_ressource = {} #corresction TD_5

    for pays in Country.query.all():
        for ressource in pays.resources:
            # si la clé (ressource) existe déjà dans le dictionnaire, alors il est simplement nécessaire 
            # d'ajouter le pays s'il n'est pas déjà présent
            if ressource.name in pays_par_ressource:
                if pays.name not in pays_par_ressource[ressource.name]:
                    pays_par_ressource[ressource.name].append(pays.name)
            # sinon il faut créer la clé et initialiser la valeur
            else:
                pays_par_ressource[ressource.name] = [pays.name]
    
    return render_template("pages/ressources.html",
        sous_titre="Ressources",
        donnees=Resources.query.paginate(page=page, per_page=app.config["RESOURCES_PER_PAGE"]),
        donnees_generales=pays_par_ressource)

# correction TD_4
@app.route("/ressources/<string:nom>")
def ressources(nom):
    ressources = []

    query =  Country.query
    ressources = query.filter(Country.name == nom).first()

    return render_template("pages/pays_ressources.html", pays=nom, ressources=ressources, sous_titre=nom)

#----------------------------------------------- EXERCICE 3 et 5 FIN -----------------------------------------------------------------------


#----------------------------------------------- EXERCICE 2 -----------------------------------------------------------------------
#exercice_2 pour seance_4
@app.route("/resources/<string:nom_pays>/<int:page>")
def ressources_par_pays(nom_pays, page=1):
    page_size = 10  
    query = Country.query.filter(Country.name == nom_pays)
    results = query.paginate(page=page, per_page=page_size)

    return render_template("pages/pays_ressources.html", pays=nom_pays, ressources=results, sous_titre=nom_pays)

#------------------------------------------------ EXERCICE 2 FIN --------------------------------------------------------------------------


@app.route("/ajout_pays/<string:id>/<string:name>/<string:type>/<string:rapide_description>")
def ajout_pays(name, id, type, rapide_description):
    nouveau_pays = Country(id=id , name=name , type=type, Introduction=rapide_description)
    db.session.add(nouveau_pays)
    db.session.commit()
    return "OK"

@app.route("/get_pays/<string:name>")
def get_pays(name):
    resultats = [Country.query.get(name)]
    return render_template("pages/generique.html", donnees=resultats)

@app.route("/suppression_pays/<string:id>")
def suppression_pays(id):

    pays = Country.query.get(id)

    db.session.delete(pays)
    db.session.commit()
    
    return "OK"

@app.route("/pays_pagination")
@app.route("/pays_pagination/<int:page>")
def pays_pagination(page=1):
    donnees = []
    query =  Country.query
    tous_resultats = query.paginate(page=page, per_page=app.config["PAYS_PER_PAGE"])
    return render_template("pages/pays_pagination.html", pagination=tous_resultats, sous_titre="Tous les pays")


