import numpy as np
from numpy.lib.function_base import delete
from typing import Text, Optional
from pydantic import BaseModel

class Item(BaseModel):
    #def __init__(self,name_item:str, quantity_item:int,key:Optional[str]) -> None:
    name:str
    quantity :int
    key :Optional[str]


class Recipe():

    def __init__(self,name_recipe:str,key_recipe= None,score=None) -> None:
       self.key_recipe= key_recipe
       self.name_recipe = name_recipe
       self.ingredients = []
       self.score=score

    def _search_ingredient(self,name_ingredient:str):
        
        for ingredient in self.ingredients:
            if ingredient.name_item == name_ingredient:
                return ingredient
        print("%s not found in recipe"%name_ingredient)
        return None
    
    def add_ingredient(self,name_ingredient:str,quantity_ingredient:int):
        ingredient_searched = self.search_ingredient(name_ingredient=name_ingredient)
      
        if ingredient_searched:
            print("%s already exist"%name_ingredient)
        else:
            mi_ingredient = Item(name_item=name_ingredient,quantity_item=quantity_ingredient)
            self.ingredients.append(mi_ingredient)
            print("El ingredient %s fue agregado"%name_ingredient)

    def delete_ingredient(self,name_ingredient:str):
        ingredient_searched = self.search_ingredient(name_ingredient=name_ingredient)
      
        if ingredient_searched:
            self.ingredients.remove(ingredient_searched)
            print("El ingredient %s se ha eliminado"%name_ingredient)
        else:
            print("El ingredient %s no existe"%name_ingredient)
    
    def show_items(self):
        for ingr in self.ingredients:
            print("ingrdiente: %s quantity: %d"%(ingr.name_item, ingr.quantity_item))
"""       

class MiLibroDerecipes():
    def __init__(self) -> None:
        self.libro = []
        self.quantity_recipes=0
    
    def _search_recipe(self,name_recipe):
        for recipe in self.libro:
            if recipe.name_recipe == name_recipe:
                return recipe
        print("%s not found in heladera"%name_recipe)
        return None
        
    def add_recipe(self,recipe:Recipe):
        
        recipe_searched = self.search_recipe(name_recipe=recipe.name_recipe)
        if recipe_searched:
            print("recipe ya existe")
        else: 
            self.libro.append(recipe)

    def delete_recipe(self,name_recipe):
        recipe_searched = self.search_recipe(name_recipe=name_recipe)
        if recipe_searched:
            self.libro.remove(recipe_searched)
        else:
            print("recipe no existe")

    def use_recipe(self,name_recipe:str,mi_heladera:MiHeladera):
        recipe_searched = self.search_recipe(name_recipe=name_recipe)
        flag_no_item=0
        missing_items=[]
        
        for ingred in recipe_searched.ingredients:
            item_searched = mi_heladera.search_item(ingred.name_item)

            if not item_searched:
                missing_items.append([ingred.name_item,ingred.quantity_item])
                flag_no_item=1
            elif item_searched.quantity_item < ingred.quantity_item:
                flag_no_item=1
                missing_items.append([ingred.name_item,ingred.quantity_item-item_searched.quantity_item])
                

        if flag_no_item:
            print("missing ingredients:",missing_items)
            return
        for ingred in recipe_searched.ingredients:
            mi_heladera.delete_item(name_item=ingred.name_item, quantity=ingred.quantity_item)

    # list recepies
        

"""