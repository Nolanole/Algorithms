#!/usr/bin/python

import math
import numpy as np

def recipe_batches(recipe, ingredients):
  np_recipe = []
  np_ingredients = []

  keys = list(recipe.keys())
  for key in keys:
    np_recipe.append(recipe[key])
    try:
      np_ingredients.append(ingredients[key])
    except KeyError:
      return 0

  np_recipe = np.array(np_recipe)
  np_ingredients = np.array(np_ingredients)
  count = 0
  enough = True
  while enough:
    np_ingredients = np_ingredients - np_recipe
    if min(np_ingredients) >= 0:
        count += 1
    else:
        enough = False
  return count


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))