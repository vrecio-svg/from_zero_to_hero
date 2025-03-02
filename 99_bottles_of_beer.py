# Write code below 💖
bottle_number = 99
remained_bottle_number = 98

for song_99_bottles_of_beer in range(99, 0, -1):
  print(f"{bottle_number} bottles of beer on the wall, {bottle_number} bottles of beer.\nTake one down and pass it around, {remained_bottle_number} bottles of beer on the wall.")
  bottle_number -= 1
  remained_bottle_number -=1


  # 99 Bottles of Beer 🍻
# Codédex

for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')