"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки:
 “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


def check_number(x):
    while x <= 1 or x > 100_000:
        print('Incorrect number. Try again.')
        x = int(input('Input again: '))
    return x


def check_prime (x):
    n = x
    count = 0
    for i in range (1, n + 1):
        if n % i == 0:
            count+=1
    if count == 2:
        print(f'The number {x} is prime')
    else:
        print(f'The number {x} is composite')

num = check_number(int(input('Input a number: ')))
check_prime(num)