import random
wordbank = ['cars']
random_choice = random.choice(wordbank)
word = " "
for letter in random_choice.strip():
  word += "_ "
print(word)


class Hangman:

    def __init__(self, word):
        self.correct_word = word.lower()
        self.guessed_letters = set([])
        self.life_count = 7
        self.output = ["_ " for ch in self.correct_word.strip()]
        self.has_game_ended = False

    def check_guess(self, letter):
        if letter in self.guessed_letters:
            print("You have already guessed this letter.")
        elif letter in self.correct_word:
            print("Correct! That letter is in the word!")
        else:
            print("Sorry, that letter is not in the word.")
            self.life_count -= 1
        self.guessed_letters.add(letter)
        print("You have", self.life_count, "lives left")

    def correct_word_found(self):
        found_no_match = False
        for letterIdx in range(len(self.output)):
            if self.output[letterIdx] in self.guessed_letters:
                found_no_match = True
            else:
                found_no_match = False
                break

        if found_no_match:
            print("You found the word")
            print("The word was", self.correct_word)
            self.has_game_ended = True

    def is_game_over(self):
        if self.life_count == 0:
            print("You lost all your lives.")
            print("The word was", self.correct_word)

    def print_word_so_far(self, letter):
        for letterIdx in range(len(self.correct_word)):
            if self.correct_word[letterIdx] == letter:
                self.output[letterIdx] = letter
        print("".join(self.output))

game = Hangman(random_choice)
while game.life_count > 0 and game.has_game_ended == False:
  guess = input("Guess a letter: ").lower()
  game.print_word_so_far(guess)
  game.check_guess(guess)
  print("\n")
  game.correct_word_found()
  game.is_game_over()
