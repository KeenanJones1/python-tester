from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import errorcode
load_dotenv()

password = os.getenv("DB_PASSWORD")
host = os.getenv("HOST")
database = os.getenv("DB_NAME")


config = {
    'user': 'root',
    'password': password,
    'host': host,
    'database': database
}

db = mysql.connector.connect(**config)
cursor = db.cursor()


# import mysql.connector
# from mysql.connector import errorcode

# config = {
#     'user': 'root',
#     'password': 'Tmacvc12!',
#     'host': 'localhost',
#     'database': 'acme'
# }

# db = mysql.connector.connect(**config)
# cursor = db.cursor()
