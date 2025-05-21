import random

player = 0
computer = 0

one = "✊"
two = "✋"
three = "✌"
four = "🦎"
five = "🖖"


print("===========================")
print("Rock Paper Scissors")
print("===========================")

print("It's time to play. Choose rock (1), paper (2), scissor (3), lizard (4) or spock (5), and let's see who is a loser.")
print("1) Rock ✊")
print("2) Paper ✋")
print("3) Scissors✌")
print("4) Lizard 🦎")
print("5) Spock 🖖")

while True:
    try:
        player = int(input("Introduce a number: "))
        if player in [1, 2, 3, 4, 5]:
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        
computer = random.randint(1,5)

if player == 1 and computer == 2:
    print("You chose ✊  and Computer chose ✋. Computer wins!")
elif player == 1 and computer == 3:
    print("You chose ✊  and Computer chose ✌. You win!")
elif player == 1 and computer == 4:
    print("You chose ✊  and Computer chose 🦎. You win!")
elif player == 1 and computer == 5:
    print("You chose ✊  and Computer chose 🖖. Computer wins!")
elif player == 2 and computer == 1:
    print("You chose ✋  and Computer chose ✊. You win!")
elif player == 2 and computer == 3:
    print("You chose ✋  and Computer chose ✌. Computer wins!")
elif player == 2 and computer == 4:
    print("You chose ✋  and Computer chose 🦎. Computer wins!")
elif player == 2 and computer == 5:
    print("You chose ✋  and Computer chose 🖖. Computer wins!")
elif player == 3 and computer == 1:
    print("You chose ✌  and Computer chose ✊. Computer wins!")
elif player == 3 and computer == 2:
    print("You chose ✌   and Computer chose ✋. You win!")
elif player == 3 and computer == 4:
    print("You chose ✌  and Computer chose 🦎. You win!")
elif player == 3 and computer == 5:
    print("You chose ✌  and Computer chose 🖖. Computer wins!")
elif player == 4 and computer == 1:
    print("You chose 🦎  and Computer chose ✊. Computer wins!")
elif player == 4 and computer == 2:
    print("You chose 🦎  and Computer chose ✋. You win!")
elif player == 4 and computer == 3:
    print("You chose 🦎  and Computer chose ✌. Computer wins!")
elif player == 4 and computer == 5:
    print("You chose 🦎  and Computer chose 🖖. You win!")
elif player == 5 and computer == 1:
    print("You chose 🖖  and Computer chose ✊. You win!")
elif player == 5 and computer == 2:
    print("You chose 🖖  and Computer chose ✋. Computer wins!")
elif player == 5 and computer == 3:
    print("You chose 🖖  and Computer chose ✌. You win!")
elif player == 5 and computer == 4:
    print("You chose 🖖  and Computer chose 🦎. Computer wins!")
else:
    print("Tie")