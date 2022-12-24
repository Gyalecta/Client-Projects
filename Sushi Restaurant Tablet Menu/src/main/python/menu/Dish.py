import json

class Dish:
  def __init__(self, name):
    with open("menu.json", "r") as file:
      menu = json.load(file)
      for category in menu:
        for dish in menu[category]:
          if dish["name"] == name:
            self.name = dish["name"]
            self.description = dish["description"]
            self.price = dish["price"]
            break
    if not hasattr(self, "name"):
      raise ValueError(f"Dish '{name}' not found in menu")

  def get_name(self):
    return self.name

  def get_description(self):
    return self.description

  def get_price(self):
    return self.price
