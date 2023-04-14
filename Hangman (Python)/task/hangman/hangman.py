import random

print("H A N G M A N")

word_list = ["python", "java", "swift", "javascript"]
winner_word = random.choice(word_list)
filler = '-' * (len(winner_word)- 3)
input_word = input(f"Guess the word {winner_word[:3] + filler}: ")

if input_word == winner_word:
    print("You survived!")
else:
    print("You lost!")
