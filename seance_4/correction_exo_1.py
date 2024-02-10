from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from model import Geography  
query = Geography.query.filter(Geography.major_aquifers == 'Congo Basin').all()



from model import Elevation
query = Elevation.query.filter(
    (Elevation.lowest_point == 'Atlantic Ocean 0 m') | (Elevation.lowest_point == 'Baltic Sea 0 m'),
    Elevation.mean_elevation != None,
    Elevation.mean_elevation != ''
).all()

#jointure
from model import Country, CountryMap, Map
query = Country.query.join(CountryMap, CountryMap.id == Country.id).join(Map, CountryMap.map_ref == Map.name).all()
#une méthode plus simple en utilisant les jointures naturelles: 
#Country.query.all() suffit car les jointures entre Country et Map via country_maps sont faites automatiquement par SQLAlchemy 
#grâce à l’attribut de relation Country.maps présent dans factbook.py
query = Country.query.all()

#selcetion des champs remenes
from model import Geography, Country
query = Geography.query.with_entities(Country.name, Geography.coordinates, Geography.climate).join(Country, Country.id == Geography.id).filter(Geography.major_aquifers == 'Congo Basin').all()

#Aggrégations
from sqlalchemy import func
from model import Country, Country_resources, Resources
query = Country.query.with_entities(Country.name, func.count(Country.id)).join(Country_resources, Country_resources.id == Country.id).join(Resources, Resources.id == Country_resources.resource).group_by(Country.id).having(func.count(Country.id) > 10).all()

#Ordonner les résultats
from model import Country, Country_resources, Resources
query = Country.query.with_entities(Country.name, Resources.name).join(Country_resources, Country_resources.id == Country.id).join(Resources, Resources.id == Country_resources.resource).order_by(Country.name.desc(), Resources.name.asc()).all()
