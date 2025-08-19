import assets
import random 

display = ""
guess = ""
correct_letters = []
guessed_letters = "" #for displayin all the guessed letters (wrong ones only)

language = input("please select a language:\nType 'en' for english\nType 'es' for spanish\nType 'de' for german\nType 'all' for a random word from any language\n").lower()
#change display messages accorgdingly as well
if language == "es":
    chosen_word = random.choice(assets.words_spanish)
elif language == "en":
    chosen_word = random.choice(assets.words_english)
elif language == "de":
    chosen_word = random.choice(assets.words_german)
elif language == "all":
    chosen_word = random.choice(assets.word_list)
else:
    print("That was not an option default to any")
    chosen_word = random.choice(assets.word_list)

#add dificulty for game (hard will start on hangman 4 and and have only 6 lives, easy the standard 10)
#Add word guesses (count only as one live)
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
    print(f"{assets.hangman_game[i]}\n\n {display}\n\n")
    if len(guessed_letters) > 0:
        print(f"not in word: {guessed_letters}")
#add valid input function (checks for multiple characters, if input is a symbol or number) Can also check repeated guesses
while assets.end_game == False:
    guess = input("Guess a letter: ").lower() # check this for multiple inputs , eg word and for numbers/symbols
    display =  update_display(display)
    if guess in chosen_word:
        print(f"{guess} is in the word")
        if "_" not in display:
            print("You win, great Job!")
            assets.end_game = True
    else:
        if guess in guessed_letters:
            print("You guessed that already")
        else:
            guessed_letters += guess + ", "
            assets.lives -= 1
        if assets.lives <= 0:
            print("Game Over")
            assets.end_game = True
        else:
            print(f"wrong number of lives remaining {assets.lives}")
    display_game()

#Necessary updates
# - Add check for valid input/guess
# - Change display messages to selected language

#Future functionality 
# - Add hard or easy mode (6 or 10 lives)
# - Add word guesses (only valid if len of word) (cost one live)
# - Integrate a dictionary/language library (no more manual created lists)
# - For defined language have choice (easy and hard) wether user want so write accents/umlaut manually or use simple method
# --> simple method would be different accoding to language
# --> e.g Spanish easy will accept 'n' for 'ñ' and 'c' for 'ç' 
# --> e.g in german you can select wether 'a' should count as 'ä' or we use the 'ae' for 'ä'(extending the word len) 
# --> e.g if there are symbols in the word these will be shown (easy mode) eg "mba'eichapa" would be "___'_______"
# - Check if we can update the terminal staticly eg clear and overwrite rather than diplay all messages below eachother