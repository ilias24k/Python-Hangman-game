import random

#opening file

f = open("words.txt")

line = f.readlines()
#storing file to list
word_list = [item.strip() for item in line]
max_guesses= 6
guesses=0
#chossing random word
word=random.choice(word_list)
#display word with asterisks
displayed_word="*" *len(word)
print("this is your word",displayed_word)

#while loop to track guesses

while  max_guesses>0:
    letter=input("enter your letter or guess the word")
    if letter.lower() not in word:
        max_guesses-=1
        print("wrong, remaining guesses:",max_guesses-guesses)

    elif letter==word:
        print("congrats you got it")
        break
    else:
        print("right")
        new_displayed_word = ''
        # parallel loop to update/display word when user enters right letter
        for w, l in zip(word, displayed_word):
            if letter.lower() == w:
                new_displayed_word += letter.lower()
            else:
                new_displayed_word += l
        displayed_word = new_displayed_word
        print(displayed_word)
        #win condition
        if not '*' in displayed_word:
            print("You won!")












