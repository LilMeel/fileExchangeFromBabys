import pymysql.cursors
import config
from datetime import datetime
# Подключиться к базе данных.

def connect():
    connection = None
    try:
        connection = pymysql.connect(host='127.0.0.1',
                                     port=3306,
                                     user='telegram_appendbd',
                                     password=f'{config.USER_PASSWORD}',
                                     db=f'{config.DB_NAME}',
                                     cursorclass=pymysql.cursors.DictCursor)
        print("DB connected!")

        cursor = connection.cursor()
    except Exception as e:
        print(f"The error '{e}' occurred")
        exit(0)
    return connection

def check(cursor, login):
    res = cursor.execute(f"SELECT * FROM users WHERE login=%s", (login,))
    if res:
        return True
    return False

def try_to_add(login, password):
    connection = connect()
    cursor = connection.cursor()
    res_str = ""
    try:
        if check(cursor, login):
            res_str = "Данный аккаунт уже существует"
            return res_str
        create_users = "INSERT INTO `users` (`login`, `password`, `signup_date`) VALUES (%s, %s, %s);"

        values = [login, password, datetime.now().strftime("%Y-%m-%d")]
        cursor.execute(create_users, values)
        connection.commit()
        res_str = f"Аккаунт {login} зарегистрирован"
    except Exception as ex:
        res_str = "Ошибка в базе данных"
        print(ex)
    finally:
        print("DB disconnected")
        connection.close()
        return res_str



