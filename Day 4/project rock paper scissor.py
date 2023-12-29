
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
user=int(input("What do you use choose? Type 0 for rock, 1 for paper or 2 for scissors \n"))
if user>=3 or user<0:
    print("INAVLID")
else:
    print(game[user])
rand=random.randint(0,2)
print(f"computer chose: \n{game[rand]}")


if user==0 and rand==2:
    print("you win")
elif rand==0 and user==2:
    print("you loose")
elif user>rand and user<3 and user>=0:
    print("you win")
elif  rand>user and user<3 and user>=0:
    print("you loose")
else:
    print("it's a draw")