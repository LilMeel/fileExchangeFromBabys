from bot_logic import start_bot
from db_connection import connect

if __name__ == '__main__':
    connect()
    start_bot()