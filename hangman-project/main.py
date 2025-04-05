import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
lives = 6

progress = ["_" for _ in chosen_word]
guess_list = []

correct_guesses = 0
game_over = False
while not game_over:
    current_index = 0
    correct = False
    guess = input("Guess a letter: ").lower()
    if guess in guess_list:
        print("You've already guessed the letter " + guess + "! Guess again")
    else:
        for letter in chosen_word:
            if letter == guess:
                progress[current_index] = letter
                correct_guesses += 1
                correct = True

            current_index += 1
        if not correct:
            lives -= 1
            print("You guessed " + guess + " and that is not in the word! A life has been lost")

    guess_list.append(guess)
    print("".join(progress))
    print(hangman_art.stages[lives])
    print(f"***************** YOU HAVE {lives} LIVES LEFT ***********************")
    if lives == 0:
        print(f"IT WAS {chosen_word.upper()}! YOU LOSE")
        game_over = True
    if "_" not in progress:
        print("Game over, you win!")
        game_over = True
