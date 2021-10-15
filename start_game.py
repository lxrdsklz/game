from source import game_start
import sqlite3

#TODO
#группировка по проебанным попыткам

if __name__ == '__main__':
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    res = game_start.start()
    SQL = '''INSERT INTO users ('username', 'failedAttempts') VALUES ('%s', '%s')''' % (res[1], res[0])
    cursor.execute(SQL)
    conn.commit()

    select = cursor.execute('''SELECT * FROM users ORDER BY failedAttempts desc''')
    print('=' * 100)
    print('Таблица лохов по убыванию \n')
    for row in select:
        print(f'Имя: {row[1]}')
        print(f'Количество попыток: {row[2]}')
        print('=' * 50)