from Model.recipe import MealType
import logging
import sys
from DataAccess.FileDataAccess import DatabaseReader
from Analysis.analyzeFunction import recipeIngredients
from flask import Flask, request, render_template

app = Flask(__name__)

# Connect to the database and load the recipes
dbData = DatabaseReader("postgres", "postgres", "purple7", "127.0.0.1", "5432")
recipe_dict = dbData.readDBRecipe()
print(dbData.readDBRecipe())

# Render the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        # Get the ingredients from the form
        ingredients = request.form['ingredients']  # Get comma-separated ingredients
        if not ingredients:
            return render_template('results.html', search_query=ingredients, recipes=[])

        # Convert the ingredients string to a list
        ingredient_list = [ingredient.strip() for ingredient in ingredients.split(',')]

        # Find recipes with the ingredients
        recipes = recipeIngredients(ingredient_list, recipe_dict)

        if not recipes:
            return render_template('results.html', search_query=ingredients, recipes=[])

        # Convert Recipe objects to a more user-friendly format for display
        recipe_list = []
        for r in recipes:
            recipe_info = {
                'name': r.name,
                'description': r.description,
                'serving_size': r.serving_size,
                'type': r.food_type.name,  # Convert MealType enum to string
                'ingredients': [{'name': i.name, 'amount': i.amount, 'type': i.type} for i in r.ingredientList]
            }
            recipe_list.append(recipe_info)

        # Render the results page with the list of recipes
        return render_template('results.html', search_query=ingredients, recipes=recipe_list)
    
    except Exception as e:
        return render_template('results.html', search_query='', recipes=[], error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
