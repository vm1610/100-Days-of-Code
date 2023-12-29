#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
#todo1
chosen_word=random.choice(word_list)
#todo2
guess =input("guess aa letter. \n").lower()
print(chosen_word)
for letter in chosen_word:
    if letter==guess:
        print("right")
    else:
        print("wrong")
