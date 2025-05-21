# Write code below 💖
import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
    results = random.choices(symbols, k=3)
    print(' | '.join(results))
    
    if all(results == '7️⃣' for symbol in results):
        print("Jackspot!")
    else:
        print("Thanks for playing!")
    
while True:
    play()
    play_again = input("Do you want to keep on playing? (Y/N): ").strip().upper()
    if play_again == "Y":
        continue
    elif play_again == "N":
        print("Okay, no problem. See you soon!")
        break
    else:
        print("Invalid input. Please enter 'Y' to play again or 'N' to quit.")