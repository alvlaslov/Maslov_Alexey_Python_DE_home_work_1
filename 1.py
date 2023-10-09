"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def check_side(x):
    while x <= 0:
        print('Incorrect number. Try again.')
        x = int(input('Input again: '))
    return x


def triangle_rull(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print(f'Triangle with side a = {a}, b = {b}, c = {c} doesnt exsist')
        return 0
    else:
        return 1


def check_triangel(a, b, c):
    if a != b and a != c and b != c:
        print(f'Triangle with side a = {a}, b = {b}, c = {c} is versatile')
    elif a == b and a != c or a == c and a != b:
        print(f'Triangle with side a = {a}, b = {b}, c = {c} is isosceles ')
    else:
        print(f'Triangle with side a = {a}, b = {b}, c = {c} is equilateral')


a_side = check_side(int(input('Input a side: ')))
b_side = check_side(int(input('Input b side: ')))
c_side = check_side(int(input('Input c side: ')))

if triangle_rull(a_side, b_side, c_side) == 1:
    check_triangel(a_side, b_side, c_side)
