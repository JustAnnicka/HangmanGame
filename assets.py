import random

words_english = ["aardvark", "baboon", "camel", "love"]
words_spanish = ["amor", "alma", "buenas", "cuchillo", "dia"]
words_german = ["antrag", "arbeit", "bett", "beton", "dienstag","liebe"]
word_list = [words_english, words_spanish, words_german]
#chosen_word = random.choice(word_list)
# word_len = len(chosen_word)
lives = 10
end_game = False

hangman_0 = '''







    _ ___ '''
hangman_1 = '''

     |
     |
     |
     |
     |
     |
    _|___ '''
hangman_2= '''
      _______
     |
     |
     |
     |
     |
     |
    _|___ '''
hangman_3= '''
      _______
     |/
     |
     |
     |
     |
     |
    _|___ '''
hangman_4= '''
      _______
     |/      |
     |
     |
     |
     |
     |
    _|___ '''
hangman_5= '''
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___ '''
hangman_6= '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
     |
    _|___ '''
hangman_7= '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      / 
     |
    _|___ '''
hangman_8= '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      / \ 
     |
    _|___ '''
hangman_9= '''
      _______
     |/      |
     |      (_)
     |      /|
     |       |
     |      / \ 
     |
    _|___ '''
hangman_10= '''
      _______
     |/      |
     |      (_)
     |      /|\ 
     |       |
     |      / \ 
     |
    _|___ '''


hangman_game = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7, hangman_8, hangman_9, hangman_10]
 #add Guarani wiht accents (will auto add symbols and accept n for ñ & etc)