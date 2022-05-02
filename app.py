import json
import imp
from flask import Blueprint
from flask_restful import Api
from contollers import StatsClass

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# import data
data_import = open('data.json')
data_input = json.load(data_import)


@api_bp.route("/")
def base_route():
    filtered = StatsClass(data_input)
    data = filtered.uniq_recipe_element()
    return data
@api_bp.route("/uniq-recipes")
def uniq_recipes():
    filtered = StatsClass(data_input)
    data = filtered.uniq_recipe_element()
    return data

@api_bp.route("/busiest-postcode")
def postal_deliveries():
    filtered = StatsClass(data_input)
    data = filtered.postal_deliveries()
    return data

@api_bp.route("/recipe-occurrence")
def recipe_occurrence():
    filtered = StatsClass(data_input)
    data = filtered.occurrence_of_recipes()
    return data

@api_bp.route("/recipe-match-name")
def recipe_match_by_name():
    filtered = StatsClass(data_input)
    data = filtered.recipe_match_by_name()
    return data
