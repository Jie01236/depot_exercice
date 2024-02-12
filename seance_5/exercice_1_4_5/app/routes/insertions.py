from ..app import app, db
from flask import render_template, request
from ..models.factbook import Country, Resources, Map
from ..models.formulaires import InsertionPays, InsertionRessource
from ..utils.transformations import  clean_arg

@app.route("/insertions/pays", methods=['GET', 'POST'])
def insertion_pays():
    form = InsertionPays() 

    if form.validate_on_submit():
        nom_pays =  clean_arg(request.form.get("nom_pays", None))
        code_pays =  clean_arg(request.form.get("code_pays", None))
        type =  clean_arg(request.form.get("type", None))
        introduction =  clean_arg(request.form.get("introduction", None))
        ressources =  clean_arg(request.form.getlist("ressources", None))
        continent =  clean_arg(request.form.get("continent", None))

        nouveau_pays = Country(id=code_pays, 
            Introduction=introduction,
            name=nom_pays,
            type = type)

        for ressource in ressources:
            ressource = Resources.\
                query.\
                filter(Resources.id == ressource).\
                first()
            nouveau_pays.resources.append(ressource)
        
        nouveau_pays.maps.append(Map.query.filter(Map.name==continent).first())

        db.session.add(nouveau_pays)
        db.session.commit()
    
    return render_template("pages/insertion_pays.html", 
            sous_titre= "Insertion pays" , 
            form=form)

#----------- exercice 1----------------------------------------------------------
@app.route("/insertions/ressource", methods=['GET', 'POST'])
def insertion_ressource():
    form = InsertionRessource() 

    if form.validate_on_submit():
        nom_ressource =  clean_arg(request.form.get("nom_ressource", None))
        code_ressource =  clean_arg(request.form.get("code_ressource", None))

        nouveau_ressource = Resources(id=code_ressource, 
            name=nom_ressource,)

        db.session.add(nouveau_ressource)
        db.session.commit()
    
    return render_template("pages/insertion_ressource.html", 
            sous_titre= "Insertion ressources" , 
            form=form)