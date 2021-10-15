def game(low_edge, high_edge, hidden_number):
    game = True
    counts = 0
    while game:
        guessing_number = int(input('Угадайте число: '))
        if guessing_number < low_edge:
            print('Число меньше допустимой нижней границы')
        elif guessing_number > high_edge:
            print('Число больше допустимой верхней границы')
        else:
            if guessing_number > hidden_number:
                print('Загаднное число меньше вашего')
            elif guessing_number < hidden_number:
                print('Загаднное число больше вашего')
            elif guessing_number == hidden_number:
                print('Вы угадали. Загаданное число было %s' % hidden_number)
                game = False
        counts += 1
        print('Количество попыток: %s' % counts)