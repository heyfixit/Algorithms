#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # find the limiting ingredient for a given recipe

  max_possible = None

  # keep track of ingredients we've used
  recipe_keys = list(recipe.keys())
  ingredient_keys = list(ingredients.keys())

  # if we have keys in recipe that aren't in ingredients,
  # we can't make anything
  if len(list(set(recipe_keys) - set(ingredient_keys))) > 0:
    return 0

  # iterate over dictionary
  for k,v in ingredients.items():

    # skip if recipe doesn't have this ingredient
    if not k in recipe:
      continue

    num_possible = v // recipe[k]
    if max_possible is None or num_possible < max_possible:
      max_possible = num_possible

  return max_possible




if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 51, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
