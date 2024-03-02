import random
ans = random.randint(1,1000)
life = 10
game_state = True
cheat_code = 1240
guess_list = []


while game_state == True:
    guess = input("Pick a number from 1 - 1000: ")
    guess = int(guess)

    if guess == cheat_code:
        print(f"Loading... \n correct, the number was {ans}")
        game_state = False
        break

    if guess == ans:
        print(f"Great job, you guessed the number it was {ans}!")
        game_state = False

    elif guess in guess_list:
        print("You already picked that number so it won't count against you \n")

    elif guess > 1000:
        print("That's not a valid answer, your guess must be below 1000 \n")

    else:
        guess_list.append(guess)
        life -= 1
        print(f"Your life count dropped to {life} be careful!")

        if ans > guess:
            print("Your guess was too low. \n")
        else:
            print("Your guess was too high. \n")

    if life == 0:
        print("You lost all your lives,game over")
        print(f"The number was {ans}")
        game_state = False