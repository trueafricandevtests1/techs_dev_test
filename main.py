from itertools import count
import json
from collections import defaultdict
from unittest import result


# import data
data_import = open('x.json')
data = json.load(data_import)


class stats_class(object):
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

    def postal_deliveries(self):
        data = self.data
        results = []
        key = 'postcode'
        for  i in data:
            post_code = i[key]
            results.append({'postcode':post_code,'delivery_count':1})

        counter = defaultdict(int)
        for d in results:
            counter[d['postcode']] +=d['delivery_count']
        filtered = [{'postcode':postcode,'delivery_count':delivery_count} for postcode,delivery_count in counter.items()]
        max_postcode_deliveries = max(filtered,key=lambda d:d['delivery_count'])
        return max_postcode_deliveries


    def occurrence_of_recipes(self):
         
        data = self.data
        results =[ ]
        key = 'recipe'
        for i in data:
            tracked_key = i[key]
            results.append({'recipe':tracked_key, 'count':1})

        counter = defaultdict(int)

        new_result = sorted(results, key=lambda d: d['recipe']) 
        for d in new_result:
            counter[d['recipe'] ] +=d['count']
        data=[{'recipe': recipe, 'count': count} for recipe, count in counter.items()]                

        return data

    def recipe_regex(self):
     
        data = self.data
       # list_recipes= [d['recipe'] for d in data]
        list_Potato= [d['recipe'] for d in data if 'Potato' in d['recipe']]
        list_Veggie = [d['recipe'] for d in data if 'Veggie' in d['recipe']]
        List_Mushroom = [d['recipe'] for d in data if 'Mushroom' in d['recipe']]
        results = list_Veggie + list_Potato +List_Mushroom
 
        return results


# call the class
stats = stats_class(data)
print(stats.uniq_recipe_element() )

print(stats.occurrence_of_recipes())


print(stats.postal_deliveries())

print(stats.recipe_regex())
