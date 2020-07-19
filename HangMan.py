import random

def hangman():
    word =  random.choice(["apple", "book", "cat", "dog", "elephant", "fan", "goat", "hen", "ice", "jug", "kite", "lion", "monkey", "next", "orange", "peacock", "queen", "rat", "sparrow", "toy", "umbrella", "van", "watch", "xray", "yak", "zebra"])
    validletter = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""

    while len(word) > 0:
        main = ""
        if main == word:
            print("You Win")
            break

name = input("Enter Your Name : ");
print(f"Welcome {name}")
print("------------------------------")
print("Try to guess the word in less than 10 attempts.")

hangman()
