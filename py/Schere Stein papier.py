
def main():
    a = ['Rock', 'Paper', 'Scissors']
    n = input('Please select 1: ')

    import random

    pc = random.choice(a)
    run = True


    while run:


        if n == pc:
            print('its a draw, the pc chose the same')
            break

        elif n == 'Rock' and pc == 'Scissors':
            print('you won, pc chose Scissors')
            break

        elif n == 'Rock' and pc == 'Paper':
            print('you lose, pc chose Paper')
            break

        elif n == 'Scissors' and pc == 'Paper':
            print('you won, pc chose Paper')
            break

        elif n == 'Paper' and pc == 'Scissors':
            print('you lose, pc chose Scissors')
            break

        elif n == 'Paper' and pc == 'Rock':
            print('you won, pc chose Rock')
            break

        elif n == 'Scissors' and pc == 'Rock':
            print('you lose, pc chose Rock')
            break

        else:
            print('invalid')
            break

main()

while True:
    anwer = input('Do you want to play again? ')
    if anwer.lower() == 'YO' or anwer.lower() == 'yes':
        main()

    else:
        break
