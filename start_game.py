from source import game_start
import sqlite3

#TODO
#группировка по проебанным попыткам

if __name__ == '__main__':
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    res = game_start.start()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY,
    username TEXT,
    failedAttempts INT)
    ''')

    SQL = '''
    INSERT INTO users ('username', 'failedAttempts') 
    VALUES ('%s', '%s')''' % (res[1], res[0])
    cursor.execute(SQL)
    conn.commit()

    score = cursor.execute('''
    SELECT * 
    FROM users 
    ORDER BY failedAttempts asc''')
    print('=' * 100)
    print('Таблица лучших игроков \n')

    for row in score:
        print(f'Имя: {row[1]}')
        print(f'Количество попыток: {row[2]}')
        print('=' * 50)

    topRated = cursor.execute('''
    SELECT COUNT(username), MIN(failedAttempts) 
    FROM users 
    GROUP BY failedAttempts    
    ''')

    for row in topRated:
        if row[0] == 1:
            print(f'Меньшее количество попыток было потрачено у {row[0]} игрока')
        elif row[0] > 1:
            print(f'Меньшее количество попыток было потрачено у {row[0]} игроков')
        print('=' * 50)
        break

    mostBad = cursor.execute('''
    SELECT username, failedAttempts 
    FROM users 
    ORDER BY failedAttempts desc
    LIMIT 1    
    ''')

    for row in mostBad:
        print(f'Больше всех попыток набрал игрок: >>> {row[0]} <<<')
        print('=' * 50)
        break