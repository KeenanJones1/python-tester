import mysql.connector
import os
from database import cursor
from mysql.connector import errorcode
database = os.getenv("DB_NAME")

TABLES = {}


TABLES['users'] = (
    "CREATE TABLE `users` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `first_name` varchar(250) NOT NULL,"
    " `last_name` varchar(250) NOT NULL,"
    " `middle_in` varchar(1),"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

# TABLES['logs'] = (
#     "CREATE TABLE `logs` ("
#     " `id` int(11) NOT NULL AUTO_INCREMENT,"
#     " `text` varchar(250) NOT NULL,"
#     " `user` varchar(250) NOT NULL,"
#     " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
#     " PRIMARY KEY (`id`)"
#     ") ENGINE=InnoDB"
# )


def create_database():
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {database} DEFAULT CHARACTER SET 'utf8' ")
    print(f"Database {database} was created!")


def create_tables():
    cursor.execute(f"USE {database}")
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(f"Creating Tables {table_name}", end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Already Exists')
            else:
                print(err.msg)


create_database()
create_tables()
