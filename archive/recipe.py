import logging
import string
from typing import List
from Model.ingredients import Ingredient
from enum import Enum, auto

class MealType(Enum):
    BREAKFAST=auto()
    LUNCH = auto()
    DINNER = auto()

class Recipe:
    logger = logging.getLogger("Recipe")
    ConsoleOutputHandler = logging.StreamHandler()

    logger.addHandler(ConsoleOutputHandler)

    def __init__(self, name: string, description, serving_size, food_type: MealType, time):
        self.name: string = name
        self.description = description
        self.serving_size = serving_size
        self.food_type:MealType = food_type
        self.time = time
        # can only be a list of Ingredient
        self.ingredientList: List[Ingredient] = []

        Recipe.logger.warning("Recipe name: " + self.name +
                           " Recipe Description: " + self.description +
                           " Recipe Serving: " + self.serving_size +
                           " Recipe type: " + self.food_type.name +
                           " Recipe Time: " + self.time)

    def __str__(self):
        retStr = f"{self.name}: {self.description} ({self.serving_size} servings, {self.food_type}, {self.time} minutes): "
        for ing in self.ingredientList:
            retStr += "\n" + ' ' + str(ing)
        return retStr + "\n"

