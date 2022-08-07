import pymysql.cursors
import config
from datetime import datetime
# Подключиться к базе данных.

connection = None


def connect():
    try:
        global connection
        connection = pymysql.connect(host='127.0.0.1',
                                     port=3306,
                                     user='telegram_appendbd',
                                     password=f'{config.USER_PASSWORD}',
                                     db=f'{config.DB_NAME}',
                                     cursorclass=pymysql.cursors.DictCursor)
        print("DB connected!")

    except Exception as e:
        print(f"The error '{e}' occurred")
        exit(0)


def is_exist(login):
    res = connection.cursor().execute(f"SELECT * FROM users WHERE login=%s", (login,))
    if res:
        return True
    return False


def try_to_add(login, password, telegram_id, num_of_question, answer):
    cursor = connection.cursor()
    res_str = ""
    try:
        create_users = "INSERT INTO `users`" \
                       " (`login`, `password`, `telegram_id`, `num_of_question`, `question_answer`, `signup_date`)" \
                       " VALUES (%s, %s, %s, %s, %s, %s);"

        values = [login, password, telegram_id, num_of_question, answer, datetime.now().strftime("%Y-%m-%d")]
        cursor.execute(create_users, values)
        connection.commit()
        res_str = f"Аккаунт {login} зарегистрирован"
    except Exception as ex:
        res_str = "Ошибка в базе данных"
        print(ex)
    finally:
        return res_str



