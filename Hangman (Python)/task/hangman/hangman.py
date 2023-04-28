import random
from string import  ascii_lowercase, ascii_letters


def update_word(win_word, g_word, g_letter):
    new_guess = ""
    for index, letter in enumerate(g_word):
        if win_word[index] == g_letter:
            new_guess += g_letter
        elif letter != "-":
            new_guess += letter
        else:
            new_guess += "-"
    return new_guess


def letter_validation(letter, guessed):
    # print(letter, guessed)
    if len(letter) != 1:
        return "Please, input a single letter."
    if letter not in ascii_lowercase or letter not in ascii_letters:
        return "Please, enter a lowercase letter from the English alphabet."
    if letter in guessed:
        return "You've already guessed this letter."
    return False


def play_game():
    attempts = 8

    word_list = ["python", "java", "swift", "javascript"]
    winner_word = random.choice(word_list)
    letters = set(winner_word)
    guessed_letters = set()
    guessed_word = '-' * len(winner_word)

    while attempts > 0:

        print(f"\n{guessed_word}")
        input_letter = input("Input a letter:")

        validation = letter_validation(input_letter, guessed_letters)
        if not validation:
            if input_letter in letters:
                guessed_word = update_word(winner_word, guessed_word, input_letter)
                guessed_letters.add(input_letter)
            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1

            if "-" not in guessed_word:
                break
        else:
            print(validation)

    if "-" in guessed_word:
        print("\nYou lost!")
        return False
    else:
        print(f"You guessed the word {guessed_word}!")
        print("You survived!")
        return True


games = 0
wins = 0
print("H A N G M A N")

while True:

    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    if menu == "play":
        wins += play_game()
        games += 1
    elif menu == "results":
        print(f"You won: {wins} times")
        print(f"You lost: {games - wins} times")
    elif menu == "exit":
        break


