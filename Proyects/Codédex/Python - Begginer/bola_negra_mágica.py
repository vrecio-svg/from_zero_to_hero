# Write code below 💖
import random

question = input("Pregunta: ")

random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Claro que sí."
elif random_number == 2:
  answer = "Me da a mí que sí."
elif random_number == 3:
  answer = "Sin duda."
elif random_number == 4:
  answer = "No lo veo muy claro, prueba otra vez."
elif random_number == 5:
  answer = "Yo que tú lo preguntaba en un rato."
elif random_number == 6:
  answer = "Mejor me lo callo."
elif random_number == 7:
  answer = "Mis fuentes me comunican que no."
elif random_number == 8:
  answer = "No tiene muy buena pinta."
elif random_number == 9:
  answer = "No sé yo, eh...."
else:
  answer = "Error."

print("Bola negra mágica: " + answer)