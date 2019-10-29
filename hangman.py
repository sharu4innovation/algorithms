import getpass

def setup():
    print("Word to be guessed:")
    word = getpass.getpass().lower()
    word = list(word)
    return word

def get_guess(guess_word):
    input_letter = input("Guess:").lower()
    if input_letter in guess_word:
        print("That letter is guess already, try another")
        get_guess(guess_word)
    else:
        return input_letter

def play(word):
    guess_word = list('_'*len(word))
    print("Word looks like:", guess_word)
    error_count = 0
    er_flag = True
    while error_count <6 and guess_word != word:
        er_flag = True
        input_letter = get_guess(guess_word)
        for l in range(len(word)):
            if input_letter == word[l]:
                er_flag = False
                guess_word[l] = input_letter
        input_letter = ''
        if er_flag:
            error_count+=1
            if(error_count != 6):
                print("Hard Luck! You have {} chances".format(6-error_count))
        else:
            print("Correct! \nNow the word looks like:", guess_word)
    if error_count == 6:
        print("Game Over!")
    else:
        print("You Got that :) :", ''.join(guess_word))

if __name__ == "__main__":
    word = setup()
    play(word)
