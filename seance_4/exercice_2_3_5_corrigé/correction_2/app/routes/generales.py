from ..app import app, db
from flask import render_template
from ..models.factbook import Country, Resources

@app.route("/resources/<string:nom_pays>/<int:page>")
def resources(nom_pays, page):
    
    tous_resultats  = db.session.\
        query(Resources).\
        select_from(Country).\
        join(Country.resources).\
        filter(Country.name == nom_pays).\
        paginate(page=page, per_page=app.config["RESOURCES_PER_PAGE"])
    return render_template("pages/resources.html", pagination=tous_resultats, sous_titre="Resources de " + nom_pays, pays=nom_pays)