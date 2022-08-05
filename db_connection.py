import pymysql.cursors
import config
import datetime
# Подключиться к базе данных.

id = 0

def connect():
    connection = None
    try:
        connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password=f'{config.USER_PASSWORD}',
                                     db=f'{config.DB_NAME}',
                                     cursorclass=pymysql.cursors.DictCursor)
        print("DB connected!")

        id_command = "SELECT MAX(`id`) FROM `users`"
        cursor = connection.cursor()
        global id
        id = cursor.execute(id)
    except Exception as e:
        print(f"The error '{e}' occurred")
        exit(0)
    return connection

def check(cursor, login, password):
    cursor.execute(f"SELECT * FROM users WHERE login={login} AND password={password}")
    return cursor.fetchone()

def try_to_add(login, password):
    connection = connect()
    connection_cursor = connect().cursor()
    try:
        if not check(connection_cursor):
            connection.close()
            return False
        create_users = f"""
        INSERT INTO
          `users` (`id`, `login`, `password`, `signup_date`)
        VALUES
          ({id}, {login}, {password}, {datetime.date.strftime("%d. %B %Y")});
        """

        connection_cursor.execute(create_users)
        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()



