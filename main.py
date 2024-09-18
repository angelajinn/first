from Model.recipe import MealType
import logging
import sys
from DataAccess.FileDataAccess import DatabaseReader
from Analysis.analyzeFunction import recipeIngredients
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

dbData = DatabaseReader("postgres", "postgres", "purple7", "127.0.0.1", "5432")
recipe_dict = dbData.readDBRecipe()
print(dbData.readDBRecipe())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        ingredients = request.form.getlist('ingredients')  # Get ingredients 
        if not ingredients:
            return jsonify({'error': 'Please provide at least one ingredient to search for recipes.'})
        
        # Find recipes with the ingredients
        recipes = recipeIngredients(ingredients, recipe_dict)
        
        if not recipes:
            return jsonify({'message': 'No recipes found with the given ingredients.'})
        
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

        return jsonify({'recipes': recipe_list})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
