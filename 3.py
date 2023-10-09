"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10
COUNT = 1

def guess_number(x,y):
    global COUNT
    global ATTEMPTS
    while COUNT < ATTEMPTS:
        if x != y and x < y:
            COUNT += 1
            print(f"You didn't guess. The number is bigger than {x}.\nAttempt {COUNT}.")
            x = int(input('Input again: '))
        elif x != y and x > y:
            COUNT += 1
            print(f"You didn't guess. The number is smaller than {x}.\nAttempt {COUNT}.")
            x = int(input('Input again: '))
        else:
            print(f'YES!YES!YES! The number is {y}. Congrats!!!')
            break
    else:
        print(f"Loser. Game Over.\nThe number is {y}!")

print()
print("The program makes a number from 0 to 1000.\n"
      "It is necessary to guess the number in 10 attempts.\n"
      "Let's go!!!")
des_num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f'Hint for verification  {des_num}') # not for use during the game
client_num = int(input(f'Attempt {COUNT}. Input number: '))
guess_number(client_num, des_num)



