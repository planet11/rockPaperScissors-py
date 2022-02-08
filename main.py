import random

user_wins = 0
com_wins = 0
draws = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input(f"----------------T Y P E----------------"
                       f"\nrock / paper / scissors or 'Q' to quit\n"
                       f"---------------------------------------\n>> ").lower()
    if user_input == "q":
        # quit()
        break

    if user_input not in options:
        continue  # if user types something not in the options

    random.num = random.randint(0,2)  # rock =1 , paper = 2, scissors = 3
    com_input = options[random.randint(0,2)]
    print(f"The computer picked {com_input}!")

    if user_input == "rock" and com_input =="scissors":
        print("You Win!")
        user_wins += 1
    elif user_input == "paper" and com_input =="rock":
        print("You Win!")
        user_wins += 1
    elif user_input == "scissors" and com_input =="paper":
        print("You Win!")
        user_wins += 1
    elif user_input == com_input:
        print("Its a Draw!")
        draws +=1
    else:
        print("The Computer Wins")
        com_wins += 1
        continue
print(f'Your Wins = {user_wins}\nComputer Wins = {com_wins}\nDraws = {draws}')
print("Bye, see you later!")