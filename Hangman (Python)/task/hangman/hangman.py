import random

print("H A N G M A N")
input_word = input("Guess the word: ")

word_list = ["python", "java", "swift", "javascript"]
winner_word = random.choice(word_list)

if input_word == winner_word:
    print("You survived!")
else:
    print("You lost!")
