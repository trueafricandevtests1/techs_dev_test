from fastapi import FastAPI
from data import *

app = FastAPI()


#Endpoint for counting the unique number or recipe names
@app.get('/unique_recipe_count')
def getUniqueRecipeCount():
    response = {'unique_recipe_count':len(set(getListRecipe()))}
    return response

#Counting the number of occurances for each recipe name   
@app.get('/count_per_recipe')
def getCountForRecipe():
    list_of_item = getListRecipe()
    recipe_dict = [{"Recipe":x,"Count":list_of_item.count(x)} for x in list_of_item]
    unique_recipe_dict = list({ item['Recipe'] : item for item in recipe_dict}.values())
    recipe_obj = {"count_per_recipe":unique_recipe_dict}
    return recipe_obj

#Getting the busiest postcode with deliveries
@app.get('/busiest_postcode')
def getBusietPostCode():
    list_of_item = getListPostCodes()
    postcode_dict = [{"postcode":x,"delivery_count":list_of_item.count(x)} for x in list_of_item]
    unique_postcode_dict = list({ item['postcode'] : item for item in postcode_dict}.values())
    
    busiest_postcode = max(unique_postcode_dict, key=lambda x:x['delivery_count'])
    return {"busiest_postcode":busiest_postcode}

#Search through by recipe names 
@app.get('/match_by_name/{recipe_name}')
def getListNamesFilter(recipe_name):
    list_recips = getListRecipe()
    x = [i for i in list_recips if recipe_name  in i ]
    return {"match_by_name":x}

