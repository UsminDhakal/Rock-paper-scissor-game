import random
def game(comp,you):
    if comp=='r':
        if you=='s':
            print("Computer won")
        elif you=='p':
            print("You won!!")
        elif you=='r':
            print('Draw, You both choose same.')
        else:
            print("Please choose either R P or S....")
    
    if comp=='p':
        if you=='r':
            print("Computer won")
        elif you=='s':
            print("You won!!")
        elif you=='p':
            print('Draw, You both choose same.')
        else:
            print("Please choose either R P or S....")

    if comp=='s':
        if you=='p':
            print("Computer won")
        elif you=='r':
            print("You won!!")
        elif you=='s':
            print('Draw, You both choose same.')
        else:
            print("Please choose either R P or S....")

randno=random.randint(1,3)


if randno==1:
    comp='r'
elif randno==2:
    comp='p'
else:
    comp='s'




you=input('Player\'s Turn: Rock(R) Paper(P) or Scissor(S)??')
print(f"Computer choose {comp}")
print(f"You choose {you}")
game(comp,you)