### ASSIGNMENT 1 ###

# TASK 1 PART 1 #
# Create a variable to hold the final sum
result_if = 0

# For-loop to run trough all the numbers below 1000
for i in range(1000):
    # If-statement to control wether a given number is divisible  
    if i%3 == 0 or i%5 == 0:
        # Add the value of a number to the sum, if conditions of if-statement are met.
        result_if += i

# Print the final result
print("\nOUTPUT TASK 1, PART 1: Sum of IF-loop =", result_if,'\n')

###############################################

#TASK 1 PART 2

# Create an iteration variable
number = 999
# Create a variable to hold the sum of the while-loop
result_while = 0

# While-loop to run as long as condition is true
while (number) != 0:
    # If-statement to control wether a given number is divisible 
    if number%3 == 0 or number%5 == 0:
        # Add the value of a number to the sum, if conditions of if-statement are met.
        result_while += number
    # Reduce iteration variable.
    number -= 1

# Print the final result
print("OUTPUT TASK 1, PART 2: Sum of WHILE-loop =", result_while,'\n')

###############################################

# TASK 2

# Variable with original 100 digit number to be tested
number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843'

# Construct a list of every digit converted to int data type
L1 = [int(i) for i in list(number)]

# Variable to hold the highest result
highest_product = 0

# For-loop to run through all the variables in the list and multiply them by the following numbers (this is not possible to do for the last 3 numbers, hence the minus 3)
for i in range(len(L1)-3):
    # If-statement to check with the product of any 4 consecutive numbers is higher than the previos highest number stored
    if L1[i] * L1[i+1] * L1[i+2] * L1[i+3] > highest_product:
        # Change the value of the result if the conditions of the IF-statement are met
        highest_product = L1[i] * L1[i+1] * L1[i+2] * L1[i+3]

# Print the final result
print("OUTPUT TASK 2: The highest product of 4 consecutive numbers in the original string =", highest_product,'\n')

###############################################

# TASK 3

# Original list of numbers to be split into odd and even numbers
list_of_numbers = [1,2,3,4,5,6,7,8,9]

# List comprehension by testing for odd numbers (not divisible by 2)
odd = [i for i in list_of_numbers if i% 2 != 0]
# List comprehension by testing for even numbers (divisible by 2)
even = [i for i in list_of_numbers if i% 2 == 0]

# Print the final result
print('OUTPUT TASK 3: Odd numbers contained in the original list are:', odd, 'and even numbers contained are:', even,'\n')

###############################################

# TASK 4

# Variable containing string to be reversed
original_string = 'copenhagen'

# Recursive function to reverse string
def string_reverse(x):
    # If-statement to end recursion after last character
    if x == '':
        return x
    # Else clause to keep passing the string minus the last character back to the function
    else:
        return x[-1:] + string_reverse(x[:-1])

# Print the final result
print('OUTPUT TASK 4:', string_reverse(original_string),'\n')

###############################################

# TASK 5, PART A

# Variable containing original string used to cunstruct words
original_string2 = 'ccgatcahctatttaaaaccctatcatastadfa'
# Variable containing original word to be constructed from above string
original_word = 'cat'
# Dictionary to be used for storing character occurances from the 'original_string2'-variable
letter_count = {}
# List to be used for storing the different ratios of characters in the original word and string variables
character_ratios = [] 

# For-loop to populate the letter_count dictionary with letter occurance in the 'original_string' variable
for c in original_string2:
    letter_count[c] = original_string2.count(c)
# For-loop iterating trough all letters in the original word 
for c in original_word:
    # Error-handling If-loop to test if a character from the word is missing in the 'original_string2'-variable, 
    # as the construction of the 'character_ratios'-variable would otherwise fail
    if original_string2.find(c) == -1:
        character_ratios.append(0)
        break
    # Else-clause to populate the 'character_ratios"-variable with the ratio of character occurance in the word and the string respectively
    else:
        character_ratios.append (letter_count[c] / original_word.count(c))

# Print the final result
print('OUTPUT TASK 5, PART A: The word "', original_word, '" can be constructed "', int(min(character_ratios)), 
'" times from the characters contained in the string "', original_string2, '"n\n', sep='')

###############################################

# TASK 5, PART B

def word_count(word, characters):

    # Dictionary to be used for storing character occurances from the 'original_string2'-variable
    letter_count = {}
    # List to be used for storing the different ratios of characters in the original word and string variables
    character_ratios = [] 
    # For-loop to populate the letter_count dictionary with letter occurance in the 'original_string' variable
    for c in characters:
        letter_count[c] = characters.count(c)
    # For-loop iterating trough all letters in the original word 
    for c in word:
        # Error-handling If-loop to test if a character from the word is missing in the 'original_string2'-variable, 
        # as the construction of the 'character_ratios'-variable would otherwise fail
        if characters.find(c) == -1:
            character_ratios.append(0)
            break
        # Else-clause to populate the 'character_ratios"-variable with the ratio of character occurance in the word and the string respectively
        else:
            character_ratios.append (letter_count[c] / word.count(c))

    # Print the final result
    print('The word "', word, '" can be constructed "', int(min(character_ratios)), 
    '" times from the characters contained in the string "', characters, '"\n', sep='')

# Test case one, executing the function with a word and a string as arguments
print('OUTPUT TASK 5, PART B, Test1:\n',end='')
word_count('test', 'rbgeetessvaavvwtvtessetqwezqpsetssetifwriknvzpeppknonseettgrtååmpnonijubttedsrvbubuhbqazqbsusetsetzwscece')
# Test case 2- same as above, but with another t added to the word to illustrate, that the function accounts for this change
print('OUTPUT TASK 5, PART B, Test2:\n',end='')
word_count('ttest', 'rbgeetessvaavvwtvtessetqwezqpsetssetifwriknvzpeppknonseettgrtååmpnonijubttedsrvbubuhbqazqbsusetsetzwscece')

###############################################

# TASK 6

# Defining the function
def words_and_numbers(str):

    # Removing spaces from the string
    str = str.replace(' ','')

    # Constructing lists to hold letter and numbers respectively
    letters = ''
    numbers = ''

    # For-loop to run through all charaters in the string.
    for i in range(len(str)):
        
        # If-loop to check whether a character is the string is a letter or a number
        if str[i].isalpha():
            letters += str[i]
        elif str[i].isnumeric():
            numbers += str[i]
        
        # If-loops to add an underscore ('_') when the coming character in the string is of another type, than the current one
        if str[i].isalpha() and (str[i+1].isnumeric() or str[i+1] in [' ',',', '-']):
            letters += '_'
        if str[i].isnumeric() and (str[i+1].isalpha() or str[i+1] in [' ',',', '-']):
            numbers += '_'
    # Construct tuple from the two lists (letters and numbers)
    x = (letters,numbers)

    # Return the tuple as outpt of the function
    return (x)

# Print the final output
print('OUTPUT TASK 6:', words_and_numbers('Copenhagen hosted Cop-09 summit at Bella Centre in 2009, \
which was attended by delegates from more than 100 countries.'))