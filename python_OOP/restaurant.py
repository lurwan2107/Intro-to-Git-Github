class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.res_nem = restaurant_name
    self.cuis_tp = cuisine_type
    
  def describe_restaurant(self):
    print(f"The name of our restaurant is {self.res_name}")
    print(f"And we have different cuisine including chicken {self.cuis_tp}")
    print(f"The full meaning of {self.res_nem} is, Katsina City Restaurant")

  def open_restaurant(self):
    print(f"\n{self.res_nem} is usually opened at exactly 10am everyday")

my_restaurant = Restaurant("KCR", "SHAWARMA")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
