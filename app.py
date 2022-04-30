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


@api_bp.route("/uniq_recipes")
def uniq_recipes():
    filtered = StatsClass(data_input)
    data = filtered.uniq_recipe_element()
    return data
