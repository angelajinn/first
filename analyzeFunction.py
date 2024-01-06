from Model.recipe import Recipe
from Model.ingredients import Ingredient
from typing import List

# strong type - specifies argument type
def countRecipe(recipeDict: {}):
    returnDictionary = {}

    for r in recipeDict.values():
        if r.food_type not in returnDictionary.keys():
            returnDictionary[r.food_type] = 1
        else:
            returnDictionary[r.food_type] += 1

    return returnDictionary

def countRecipeIngre(recipeDict: {}):
    returnDictionary = {}

    for r in recipeDict.values():
        for j in r.ingredientList:
            if j.type not in returnDictionary.keys():
                returnDictionary[j.type] = 1
            else:
                returnDictionary[j.type] += 1

    return returnDictionary

def recipeIngredients(ingreToSearch: List[str], recipeDict: {}):
    retListRecipe: List[Recipe] = []

    for r in recipeDict.values():
        isThisRecipe = False
        for i in ingreToSearch:
            found = False
            for k in r.ingredientList:
                if i == k.name:
                    found = True
                    break
            if not found:
                break

            if i == ingreToSearch[len(ingreToSearch) - 1] and found: # If the last ing2search is found in the recipe's ingList, then the finding operation concluded.
                isThisRecipe = True
                break
        if not isThisRecipe:
            continue
        else:
            retListRecipe.append(r)

    return retListRecipe







