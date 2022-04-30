
import json
import pandas as pd


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
