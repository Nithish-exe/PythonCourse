import random

option = ["rock", "paper", "scissors"]
game_state = True

def win_or_lose(player_choice, cpu_choice):
    if player_choice == 'rock' and cpu_choice == 'rock':
        print("It's a tie!")
    elif player_choice == 'rock' and cpu_choice == 'paper':
        print("Paper covers rock, you lose...")
    elif player_choice == 'rock' and cpu_choice == 'scissors':
        print("Rock smashes scissors, you won!")
    elif player_choice == 'paper' and cpu_choice == 'paper':
        print("It's a tie!")
    elif player_choice == 'paper' and cpu_choice == 'scissors':
        print("Scissor cuts paper, you lose...")
    elif player_choice == 'paper' and cpu_choice == 'rock':
        print("Paper covers rock, you win!")
    elif player_choice == 'scissors' and cpu_choice == 'scissors':
        print("It's a tie!")
    elif player_choice == 'scissors' and cpu_choice == 'rock':
        print("Rock smashes scissors, you lost...")
    elif player_choice == 'scissors' and cpu_choice == 'paper':
        print("Scissor cuts paper, you won!")


while game_state == True:
    cpu_choice = random.choice(option)
    player_choice = input("Please choose 'rock', 'paper', or 'scissors: ")

    win_or_lose(player_choice, cpu_choice)

    play_again = input("\n Would you like to play again y/n: ")
    if play_again == 'y':
        game_state = True
    elif play_again == 'n':
        print("See you later!")
        game_state = False
    else:
        print("Invalid action, bye!")
        game_state = False

