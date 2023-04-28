import random


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


attempts = 8
print(f"H A N G M A N")

word_list = ["python", "java", "swift", "javascript"]
winner_word = random.choice(word_list)
letters = set(winner_word)
guessed_word = '-' * len(winner_word)

while attempts > 0:

    print()
    print(guessed_word)
    input_letter = input("Input a letter:")

    if input_letter in guessed_word:
        print("No improvements")
        attempts -= 1
    elif input_letter in letters:
        guessed_word = update_word(winner_word, guessed_word, input_letter)
    else:
        print("That letter doesn't appear in the word.")
        attempts -= 1

    if "-" not in guessed_word:
        print(f"\n{guessed_word}")
        print("You guessed the word!")
        break

if "-" in guessed_word:
    print("\nYou lost!")
else:
    print("You survived!")
