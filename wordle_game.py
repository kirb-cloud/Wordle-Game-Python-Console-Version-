import string

WORD_LENGTH = 5

# 1.
def read_dictionary(file_name):
    new_dictionary_list = []

    # open the file
    file = open(file_name, 'r')
    # read line in file
    for line in file:
        # remove newline characters(\n) and convert each word to lowercase
        word = line.strip().lower()
        # add the word to the dictionary list
        new_dictionary_list.append(word)
    # close file
    file.close()
    return new_dictionary_list # a list of strings with lowercase letters

# test the function
#words_list = read_dictionary('project4_dictionary.txt')
# output should be: ['skill', 'skull', 'movie', 'apple',..., 'end']
#print(words_list)


# 2. (function does not check length)
def enter_a_word (word_type, num_letters):

    # your code goes here:
    # ask user to input a_word where xxx corresponds to num_letters and www gets the value of word_type
    a_word = input(f'Enter the {num_letters}-letter {word_type} word: ')
    # convert a_word to lowercase
    a_word = a_word.strip().lower()

    return a_word  # a string with lowercase letters

# test the function
# print(enter_a_word('any', 3))
# output should be: Enter the 3-letter any word: THE
#           the


# 3.
def is_it_a_word (input_word, dictionary_list):
    # verify if input_word is present in the dictionary_list
    if input_word in dictionary_list:
        is_word = True # replace the right-hand side with the correct instructions, use indentation if needed
    # the latter part of the condition if the word is not in the list
    else:
        is_word = False

    return is_word # Boolean variable

# test the function:
# print(is_it_a_word('abcd', ['apple', 'banana'])) # output: False
# print(is_it_a_word('apple', ['apple', 'banana'])) # output: True


# 4.
def enter_and_check(word_type, dictionary_list):
    in_word = ''
    in_dict = 0
    length = 0

    # Prompts the user to enter a word in_word (using enter_a_word function) and checks both length and dictionary validity (using is_it_a_word function)
    # set as true
    while True:
       in_word = enter_a_word(word_type, 5)
       if len(in_word) == 0:
           print(f"You entered a 0-letter word that is not in the dictionary. Please try again!")
        # if the in_word is not present, user attempts again
       elif not is_it_a_word(in_word, dictionary_list):
           print(f"You entered a {len(in_word)}-letter word that is not in the dictionary. Please try again!")
        # if in_word has an incorrect length, user attempts again
       elif len(in_word) != 5:
           print(f"You entered a {len(in_word)}-letter word that is in the dictionary but with insufficient character length. Please try again!")
       else:
            # if in_word is 5 letters and is a valid word
           return in_word # a string - valid input word

# test the function
#words_list = read_dictionary('project4_dictionary.txt')
#print(enter_and_check('secret', words_list))


# 5.
remaining_alphabet = []
in_secret_word_correct_spot = []
in_secret_word_somewhere = []
not_in_secret_word = []

def compare_words (player, secret):
    global remaining_alphabet
    global in_secret_word_correct_spot
    global in_secret_word_somewhere
    global not_in_secret_word

    final = '' # replace the right-hand side with the correct instructions, use indentation if needed
    in_correct_spot = 0 # replace the right-hand side with the correct instructions, use indentation if needed

    # check if letter is in the correct spot assuming the letter is present in secret
    for i in range(len(player)):
        if player[i] == secret[i]: # if the letter is in the correct spot
            final += player[i] # add the correct letter to the final
            in_correct_spot += 1 # increment
            # also add it to in_secret_word
            if player[i] not in in_secret_word_correct_spot:
                in_secret_word_correct_spot.append(player[i])
            # remove the remaining letters from the attempt that do not meet the conditions
            if player[i] in remaining_alphabet:
                remaining_alphabet.remove(player[i])
        else:
            final += '_' # '_' used to note that the letter is not present in incorrect spot

    # check if letter is correct in the wrong spot assuming the letter is present in secret
    for i in range(len(player)):
        if player[i] != secret[i] and player[i] in secret: # if the letter is correct but in wrong spot
            if player[i] not in in_secret_word_somewhere:
                # append to in_secret_word_somewhere
                in_secret_word_somewhere.append(player[i])
            # removing remaining letters
            if player[i] in remaining_alphabet:
                remaining_alphabet.remove(player[i])

    # check if letter is not present in secret word
    for i in range(len(player)):
        if player[i] not in secret and player[i] not in not_in_secret_word:
            not_in_secret_word.append(player[i])

    return final, in_correct_spot

# test the function
# final_word, letter_in_the_right_spot = compare_words('abc',
# '123')
# print(final_word, letter_in_the_right_spot)
# output: ___ 0

### MAIN GAME CODE ###
print('Welcome to Wordle!')

alphabet_string = string.ascii_lowercase # create a string of all lowercase letters

# Initializes the lists
remaining_alphabet = list(alphabet_string)
in_secret_word_correct_spot = []
in_secret_word_somewhere = []
not_in_secret_word = []

# create a list of all valid English words words_list from project4_dictionary.txt
# using read_dictionary function.
words_list = read_dictionary('project4_dictionary.txt')

# asking the 1st user to enter the secret word using enter and check function
secret_word = enter_and_check('secret', words_list)

# initialize attempts
attempts = 0
# ask 1st user to input number of attempts
N = int(input('Input allowed number of attempts: '))

correct_guess = False

# Loop for Player 2's guesses
while attempts < N and not correct_guess:
    print(f"Enter your attempt #{attempts + 1}")

    # ask the 2nd user to make their guess
    player_word = enter_and_check('player', words_list)

    # compare the player guess with the secret word
    final_word, letter_in_the_right_spot = compare_words(player_word, secret_word)

    # output the feedback to Player 2
    print(f"letter in the right spot: {letter_in_the_right_spot}")
    print(f"You guessed letters of the secret_word: {final_word}")

    # display the history of letters guessed
    print(f"Previously attempted letters that are in the correct spot of secret_word:")
    print(in_secret_word_correct_spot)

    print(f"Previously attempted letters that are in some spot of secret_word:")
    print(in_secret_word_somewhere)

    print(f"Previously attempted letters that are not in the secret_word:")
    print(not_in_secret_word)

    # display remaining alphabet
    remaining_alphabet = [letter for letter in remaining_alphabet if letter not in not_in_secret_word and letter not in in_secret_word_correct_spot and letter not in in_secret_word_somewhere]
    print(f"Remaining letters of the alphabet that have not been tried:")
    print(remaining_alphabet)

    # if secret word is found
    if letter_in_the_right_spot == WORD_LENGTH:
        print(f"Congrats! You won using {attempts + 1} attempt(s)!")
        correct_guess = True
        break

    # track number of attempts
    attempts += 1

# exhausts all attempts
if not correct_guess:
    print(f"You already used {N} attempts. Better luck tomorrow!")