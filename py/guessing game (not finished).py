
def main():
    print('Welcome to the Guessing Game!')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random
r = random.choice(a)
move = 0
while move != 'exit' and move != r:
    move = int(input('Chose an number between 1 and 9: '))
    try:
        move = int(move)
        if move > 0 and move < 10:
            run = False
        else:
            print('the number has to between 1 and 9!!!!')

        if move < r:
            input('you are to low ^^, go on: ')

        elif move > r:
            input('you are to high UwU, go on: ')

        else:
            print('you won')
    except:
        print('you have to use a Number, not a fking letter')


main()


while True:
    anwer = input('do you want to play again?: ')
    if anwer.lower() == 'y' or anwer.lower() == 'yes':
        main()
    if anwer.lower() == 'exit':
        break
