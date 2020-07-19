# import random
from random import randint

word_list =["apple", "book", "cat", "dog", "elephant", "fan", "goat", "hen", "ice", "jug", "kite", "lion", "monkey", "next", "orange", "peacock", "queen", "rat", "sparrow", "toy", "umbrella", "van", "watch", "xray", "yak", "zebra"]
guess_word = word_list[randint(0, len(word_list)-1)]
guess_word = "apple"

print(guess_word)
guess = ["-" for i in range(len(guess_word))]

counter = 1
def guess_word_fun(count):
    global counter
    print(f"Guess the word : ", end="")
    for i in guess:
        print(i, end="")
    letter = input("\nEnter a character : ")
    if letter in guess_word:
        index1 = guess_word.index(letter)
        index2 = guess_word.rindex(letter)
        guess[index1] = letter
        guess[index2] = letter

    else:
        if(count == 1):
            print("9 turns are left")
            print("     ----------")
            counter = counter + 1
        elif(count == 2):
            print("8 turns are left")
            print("     ----------")
            print("       O")
            counter = counter + 1
        elif(count == 3):
            print("7 turns are left")
            print("     ----------")
            print("       O")
            print("       |")
            counter = counter + 1
        elif(count == 4):
            print("6 turns are left")
            print("     ----------")
            print("       O")
            print("       |")
            print("      /")
            counter = counter + 1
        elif(count == 5):
            print("5 turns are left")
            print("     ----------")
            print("       O")
            print("       |")
            print("      / \\")
            counter = counter + 1
        elif(count == 6):
            print("4 turns are left")
            print("     ----------")
            print("     \ O")
            print("       |")
            print("      / \\")
            counter = counter + 1
        elif(count == 7):
            print("3 turns are left")
            print("     ----------")
            print("     \ O /")
            print("       |")
            print("      / \\")
            counter = counter + 1
        elif(count == 8):
            print("2 turns are left")
            print("     ----------")
            print("            |")
            print("     \ O /  |")
            print("       |")
            print("      / \\")
            counter = counter + 1
        elif(count == 9):
            print("1 turns are left")
            print("     ----------")
            print("            |")
            print("     \ O / _|")
            print("       |")
            print("      / \\")
            counter = counter + 1
        elif(count == 10):
            print("You losses, you let a kind man die!")
            print("     ----------")
            print("           |")
            print("       O___|")
            print("      /|\\")
            print("      / \\")
            print("------Die-----")
            counter = counter + 1


while(counter <= 10):
    result = ""
    for i in guess:
        result = result + i
    if(guess_word == result):
        print("You Win")
        break
    guess_word_fun(counter)







# name = input("Enter your name : ")
# print(f"Welcome {name}")
# print("----------------------------------")
# print("Try to guess the word in less than 10 attempts")
