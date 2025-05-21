# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f"{self.name}")

  def display_details(self):
    print(f"Entry number: {self.entry}")
    print(f"Name: {self.name}")
    print(f"Type: {self.types}")
    print(f"Description: {self.description}")
    if self.is_caught == True:
        print(f"{self.name} has already been caught.")
    else:
        print(f"{self.name} hasn't been caught yet.")
            
pikachu = Pokemon(25, "Pikachu", "Electric", "It raises its tail to check its surroundings. The tail is sometimes struck by lightning in this pose.", False)
ninetales = Pokemon(38, "Ninetales", "Fire", "Its nine beautiful tails are filled with a wondrous energy that could keep it alive for 1,000 years.", True)
machop = Pokemon (66, "Machop", "Fight", "It loves to work out and build its muscles. It is never satisfied, even if it trains hard all day long.", False)

pikachu.speak()
pikachu.display_details()

ninetales.speak()
ninetales.display_details()

machop.speak()
machop.display_details()