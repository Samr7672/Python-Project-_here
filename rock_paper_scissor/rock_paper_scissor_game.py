import random

done=False
win, lose, tie = 0, 0, 0
names={"rock": "R", "paper": "P", "scissors": "S"}
loses={"R": "S", "P": "R", "S": "P"}
wins={"R": "P", "P": "S", "S": "R"}
user_score, computer_score = 0, 0
while not done:
    user_choice = input("Enter a choice (R, P, S):and enter 'q' to quit ").upper()
    if user_choice == "Q":
        print(f"You have {user_score} points and computer has {computer_score} points")
        break
    computer_choice = random.choice(["R", "P", "S"])
    print(f"You chose {user_choice}, computer chose {computer_choice}")
    if user_choice == computer_choice:
        print(f"It's a tie!  you choose {user_choice}, computer chose {computer_choice}. You have {user_score} points and computer has {computer_score} points")
    elif user_choice == loses[computer_choice]:
        print(f"You win! you choose {user_choice}, computer chose {computer_choice}. You have {user_score} points and computer has {computer_score} points")
        user_score += 1
        win += 1
    elif user_choice == loses[computer_choice]:
        print(f"You lose! you choose {user_choice}, computer chose {computer_choice}. You have {user_score} points and computer has {computer_score} points")
        computer_score += 1
        lose += 1
    else:
        print(f"You win! you choose {user_choice}, computer chose {computer_choice}. You have {user_score} points and computer has {computer_score} points")
        user_score += 1
        win += 1
        done=True