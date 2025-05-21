# Write code below 💖

def welcome():
  print("Welcome to our lovely coffee shop ❤️")
  print("What would you like to order?")
  print("============================")
  print("1 = 🍔 Cheeseburger")
  print("2 = 🍟 Fries")
  print("3 = 🥤 Soda")
  print("4 = 🍦 Ice Cream")
  print("5 = 🍪 Cookie")
  print("============================")

def get_user_input():
  return int(input("Please, select numbers to order: "))

def main_program(question):
  if question == 1:
    answer = "🍔 Cheeseburger"
  elif question == 2:
    answer = "🍟 Fries"
  elif question == 3:
    answer = "🥤 Soda"
  elif question == 4:
    answer = "🍦 Ice Cream"
  elif question == 5:
    answer = "🍪 Cookie"
  else:
    print("Invalid choice. Please select a number from the menu.")
  print(f"Your order: {answer}")

welcome()
user_order = get_user_input()
main_program(user_order)