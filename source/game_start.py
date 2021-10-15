import random
from source import engine


def start():
    low_edge = int(input('Нижняя граница: '))
    high_edge = int(input('Верхняя граница: '))

    hidden_number = random.randint(low_edge, high_edge)

    print('Угадайте число от %s до %s' % (low_edge, high_edge))

    engine.game(low_edge, high_edge, hidden_number)