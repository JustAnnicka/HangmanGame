import assets
import random 

display = ""
guess = ""
correct_letters = []

language = input("please select a language:\nType 'en' for english\nType 'es' for spanish\nType 'de' for german\nType 'all' for a random word from any language\n").lower()
#change display messages accorgdingly as well
if language == "es":
    chosen_word = random.choice(assets.words_spanish)
elif language == "en":
    chosen_word = random.choice(assets.words_english)
elif language == "de":
    chosen_word = random.choice(assets.words_german)
elif language == "any":
    chosen_word = random.choice(assets.word_list)
else:
    print("That was not an option default to any")
    chosen_word = random.choice(assets.word_list)

word_len = len(chosen_word)
for position in range(word_len):
    display += "-"

print(display)

def update_display(display):
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    return (display)

def display_game():
    i =  10 - assets.lives
    print(f"{assets.hangman_game[i]}\n\n {display}")
    
while assets.end_game == False:
    guess = input("Guess a letter: ").lower() # check this for multiple inputs , eg word and for numbers/symbols
    display =  update_display(display)
    if guess in chosen_word:
        print(f"{guess} is in the word")
        if "_" not in display:
            print("You win, great Job!")
            assets.end_game = True
    else:
        assets.lives -= 1
        if assets.lives <= 0:
            print("Game Over")
            assets.end_game = True
        else:
            print(f"wrong number of lives remaining {assets.lives}")
    display_game()
