from Model.recipe import MealType
import logging
from DataAccess.FileDataAccess import CsvRecipeReader
from Analysis.analyzeFunction import countRecipe
from Analysis.analyzeFunction import countRecipeIngre
from Analysis.analyzeFunction import recipeIngredients

logger = logging.getLogger("Main")
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)

csvRecipeReader = CsvRecipeReader("Resources/recipe.csv", "Resources/ingredients.csv")
recipeDict = csvRecipeReader.readRecipeDictionary()

# Print out Recipe and Ingredient objects
print(recipeDict)
print(countRecipe(recipeDict))
print(countRecipeIngre(recipeDict))


list = recipeIngredients(["onion"], recipeDict)
for i in list:
    print (i)

logger.warning("END")

