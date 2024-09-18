import csv
from Model.recipe import Recipe
from Model.ingredients import Ingredient
from Model.recipe import MealType
import logging
import traceback
def readCSVFile (filename):
    data = list(csv.reader(open(filename)))
    return data

class CsvRecipeReader:
    logger = logging.getLogger("CsvRecipeReader")
    ConsoleOutputHandler = logging.StreamHandler()
    logger.addHandler(ConsoleOutputHandler)

    # store basic information in constructor
    def __init__(self, rcpFileName, ingFileName):
        self.rcpFileName = rcpFileName
        self.ingFileName = ingFileName

    # do tasks in another function
    def readRecipeDictionary(self):
        # Read in csv file content into memory (simple data object)
        recipeDataList = readCSVFile(self.rcpFileName)
        ingredientDataList = readCSVFile(self.ingFileName)

        recipeDictionary = {}

        index = 0
        # Convert read in csv data to Recipe and Ingredient objects
        for r in recipeDataList:
            if index == 0:
                pass
            else:
                try:
                    recipeDictionary[r[0]] = (Recipe(r[0],
                                             r[1],
                                             r[2],
                                             MealType[r[3].upper()],
                                             r[4])
                                            )
                except KeyError as enumError:
                    print(type(enumError))  # type of error
                    print("the enum key cannot be found: " + str(enumError) + ". This row is skipped")  # error message
                    print(traceback.format_exc())  # location of error
                    continue
            index += 1

        index = 0
        for j in ingredientDataList:
            if index == 0:
                pass
            else:
                theIngredient = Ingredient(j[0],
                                           j[1],
                                           j[2]
                                           )

                # ** using a dictionary to find a key is faster than using a loop **
                if j[3] in recipeDictionary.keys():
                    # get value of j3 in recipe dictionary and append onto ingredient list
                    recipeDictionary[j[3]].ingredientList.append(theIngredient)
                    # print (str(theIngredient))
                else:
                    CsvRecipeReader.logger.error("Could not found:...." + str(theIngredient))
            index += 1

        return recipeDictionary

