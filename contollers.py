
import json
import pandas as pd
from collections import defaultdict


class StatsClass(object):

    def __init__(self, data):
        self.data = data

    def uniq_recipe_element(self):
        data = self.data
        arr_uniq_recipes = []

        for i in range(len(data)):
            x = data[i]['recipe']

            if i == 0:
                arr_uniq_recipes.append(x)
            elif i != 0 and x not in arr_uniq_recipes:
                arr_uniq_recipes.append(x)

        filtered = {'unique_recipe_count': len(arr_uniq_recipes)}
        return filtered

    def postal(self):
        data = self.data
        print('here')
    def occurrence_of_recipes(self):
         
        data = self.data
        results =[ ]
        key = 'recipe'
        for line in data:
            tracked_key = line[key]
            results.append({'recipe':tracked_key, 'count':1})

        counter = defaultdict(int)

        nee_result = sorted(results, key=lambda d: d['recipe']) 
        for d in nee_result:
            counter[d['recipe'] ] +=d['count']
        data=[{'recipe': recipe, 'count': count} for recipe, count in counter.items()]                

        return {"count_per_recipe":data}




    
