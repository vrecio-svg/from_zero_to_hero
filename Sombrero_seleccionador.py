# Write code below 💖
gryffindor = "🦁 Gryffindor"
ravenclaw = "🦅 Ravenclaw"
hufflepuff = "🦡 Hufflepuff"
slytherin = "🐍 Slytherin"

gryffindor_score = 0
ravenclaw_score = 0
hufflepuff_score = 0
slytherin_score = 0

print('===============')
print('The Sorting Hat')
print('===============')

print("Q1. Do you like Dawn or Dusk?\n1. Dawn\n2. Dusk")
answer_1 = int(input("Enter your answer (1-2): "))

if answer_1 == 1:
  gryffindor_score += 1
  ravenclaw_score += 1
elif answer_1 == 2:
  hufflepuff_score += 1
  slytherin_score += 1
else:
  print("Wrong input.")

print("Q2. When I'm dead, I want people to remember me as:\n1. The Good\n2. The Great\n3. The Wise\n4. The Bold")
answer_2 = int(input("Enter your answer (1-4): "))

if answer_2 == 1:
  hufflepuff_score += 1
elif answer_2 == 2:
  slytherin_score += 1
elif answer_2 == 3:
  ravenclaw_score += 1
elif answer_2 == 4:
  gryffindor_score += 1
else:
  print("Wrong input.")

print("Q3. Which kind of instrument most pleases your ear?:\n1. The violin\n2. The trumpet\n3. The piano\n4. The drum")
answer_3 = int(input("Enter your answer (1-4): "))

if answer_3 == 1:
  slytherin_score += 4
elif answer_3 == 2:
  hufflepuff_score += 4
elif answer_3 == 3:
  ravenclaw_score += 4
elif answer_3 == 4:
  gryffindor_score += 4
else:
  print("Wrong input.")

scores = {
    gryffindor: gryffindor_score,
    ravenclaw: ravenclaw_score,
    hufflepuff: hufflepuff_score,
    slytherin: slytherin_score,
}

winner_house = max(scores, key=scores.get)

print(f"¡Congrats, you are a member of: {winner_house}!")