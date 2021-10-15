import random
from source import engine


def start():
    ok = True
    while ok:
        try:
            uname = input('Введите ваше имя: ')
            low_edge = int(input('Нижняя граница: '))
            high_edge = int(input('Верхняя граница: '))

            hidden_number = random.randint(low_edge, high_edge)

            print('Угадайте число от %s до %s' % (low_edge, high_edge))

            counts = engine.game(low_edge, high_edge, hidden_number, uname)
            return [counts, uname]
        except ValueError as e:
            print('Укажите число!')
            ok = True