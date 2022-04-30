from itertools import count
import json

# import data
data_import = open('data.json')
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

    def postal(self):
        data = self.data

    def occurrence_of_recipes(self):
        data = self.data
        finalList = []

        for i in range(len(data)):
            if i == 0:
                recipe_count = {'delivery': data[i]['delivery'],
                                'recipe': data[i]['recipe'], 'postcode': data[i]['postcode'], 'count': 1}
                finalList.append(recipe_count)

            elif i != 0:
                '''
                and [lst['count'] + 1 for lst in finalList if lst['recipe']
                           == data[i]['recipe']]:
                print(i)
                '''

                for v in range(len(finalList)):
                    if finalList[v]['recipe'] != data[i]['recipe']:
                        recipe_count = {'delivery': data[i]['delivery'],
                                        'recipe': data[i]['recipe'], 'postcode': data[i]['postcode'], 'count': 1}
                        finalList.append(recipe_count)
                for v in range(len(finalList)):
                    if finalList[v]['recipe'] == data[i]['recipe']:
                        finalList[v]['count'] = finalList[v]['count']+1
                i = +1
        print(finalList)


# call the class
stats = stats_class(data)
print(stats.uniq_recipe_element()
      )
print(stats.occurrence_of_recipes())
