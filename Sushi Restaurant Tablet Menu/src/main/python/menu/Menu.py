import json
from Dish import Dish

class Menu:
  def __init__(self):
    self.dishes = []
    with open("menu.json", "r") as file:
      menu = json.load(file)
      for category in menu:
        for dish in menu[category]:
          self.dishes.append(Dish(dish["name"]))

  def add_dish(self, dish):
    if isinstance(dish, Dish):
      self.dishes.append(dish)
    else:
      raise TypeError("Invalid dish type")

  def remove_dish(self, dish_name):
    for i, dish in enumerate(self.dishes):
      if dish.get_name() == dish_name:
        self.dishes.pop(i)
        return
    raise ValueError(f"Dish '{dish_name}' not found in menu")

  def get_dishes(self):
    return self.dishes
