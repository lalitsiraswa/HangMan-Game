import random

def hangman():
    word =  random.choice(["apple", "book", "cat", "dog", "elephant", "fan", "goat", "hen", "ice", "jug", "kite", "lion", "monkey", "next", "orange", "peacock", "queen", "rat", "sparrow", "toy", "umbrella", "van", "watch", "xray", "yak", "zebra"])
    validletter = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""
    word = "apple"
    print(word)
    
    while len(word) > 0:
        main = ""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print("You Win")
            break

        print(f"Guess the word [a-z] : {main}")
        guess = input()
        
        if guess in validletter:
            if guess in word:
                guessmade = guessmade + guess
            else:
                if(turns == 10):
                    print("9 turns are left")
                    print("     ----------")
                    turns = turns - 1
                elif(turns == 9):
                    print("8 turns are left")
                    print("     ----------")
                    print("       O")
                    turns = turns - 1
                elif(turns == 8):
                    print("7 turns are left")
                    print("     ----------")
                    print("       O")
                    print("       |")
                    turns = turns - 1
                elif(turns == 7):
                    print("6 turns are left")
                    print("     ----------")
                    print("       O")
                    print("       |")
                    print("      /")
                    turns = turns - 1
                elif(turns == 6):
                    print("5 turns are left")
                    print("     ----------")
                    print("       O")
                    print("       |")
                    print("      / \\")
                    turns = turns - 1
                elif(turns == 5):
                    print("4 turns are left")
                    print("     ----------")
                    print("     \ O")
                    print("       |")
                    print("      / \\")
                    turns = turns - 1
                elif(turns == 4):
                    print("3 turns are left")
                    print("     ----------")
                    print("     \ O /")
                    print("       |")
                    print("      / \\")
                    turns = turns - 1
                elif(turns == 3):
                    print("2 turns are left")
                    print("     ----------")
                    print("            |")
                    print("     \ O /  |")
                    print("       |")
                    print("      / \\")
                    turns = turns - 1
                elif(turns == 2):
                    print("1 turns are left")
                    print("     ----------")
                    print("            |")
                    print("     \ O / _|")
                    print("       |")
                    print("      / \\")
                    turns = turns - 1
                elif(turns == 1):
                    print("You losses, you let a kind man die!")
                    print("     ----------")
                    print("           |")
                    print("       O___|")
                    print("      /|\\")
                    print("      / \\")
                    print("------Die-----")
                    turns = turns - 1    
                    break   
        else:
            print("Enter a Valid letter : ")
            guess = input()





# name = input("Enter Your Name : ");
# print(f"Welcome {name}")
# print("------------------------------")
# print("Try to guess the word in less than 10 attempts.")
hangman()