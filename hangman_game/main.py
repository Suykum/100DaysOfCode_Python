import random
import hangman_game.hangman_art as hangman_art
import hangman_game.hangman_words as hangman_words
#from replit import clear

print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(chosen_word)
display = ['_' for n in chosen_word]
lives = 6
end_of_game = False
entered_letters = []

while(not end_of_game):
  guess = (input("Guess a letter: ")).lower()
  #clear()
  if guess in display:
    print(f"You've already guessed {guess}")
  else:
    entered_letters.append(guess)

  for position in range(0, len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = guess

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      print ("You lose!")
      end_of_game = True

  print(f"{' '.join(display)}")
  print(hangman_art.stages[lives])

  if "_" not in display:
    end_of_game = True
    print("You win.")

