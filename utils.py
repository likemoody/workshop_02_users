from psycopg2 import connect

from main import logger


class DatabaseUtils:
    DB_USERNAME = "jeronimoprogrammer"  # use 'postgres' / [your username]
    DB_PASSWORD = "coderslab"

    DB_HOSTNAME = "127.0.0.1"
    DB_NAME = "postgres"

    QUERY_CREATE_DATABASE = """CREATE DATABASE {};"""
    QUERY_DROP_DATABASE = """DROP DATABASE IF EXISTS {};"""
    QUERY_CREATE_TABLE = """CREATE TABLE {};"""
    QUERY_INSERT_INTO = """INSERT INTO {} ({}) VALUES ({});"""
    QUERY_SELECT = """SELECT {} FROM {} WHERE {};"""

    @staticmethod
    def close_cursor(cursor):
        cursor.close()

    @staticmethod
    def connect_to_database(db_name):
        try:
            connection = connect(
                user=DatabaseUtils.DB_USERNAME,
                password=DatabaseUtils.DB_PASSWORD,
                host=DatabaseUtils.DB_HOSTNAME,
                database=db_name
            )
            connection.autocommit = True
            logger.info("Connect with database succeed")
            return connection
        except Exception as e:
            logger.error("Connect with database failed, {}".format(e))

    @staticmethod
    def create_database(cursor, name):
        try:
            cursor.execute(DatabaseUtils.QUERY_CREATE_DATABASE.format(name))
        except Exception as e:
            logger.error("'Create database failed, {}'".format(e))

    @staticmethod
    def drop_database(cursor, name):
        try:
            cursor.execute(DatabaseUtils.QUERY_DROP_DATABASE.format(name))
        except Exception as e:
            logger.error("'Drop database failed, {}'".format(e))

    @staticmethod
    def create_table(cursor, content):
        try:
            cursor.execute(DatabaseUtils.QUERY_CREATE_TABLE.format(content))
        except Exception as e:
            logger.error("Create table failed, {}".format(e))

    @staticmethod
    def execute_command(cursor, sql_command):
        try:
            cursor.execute(sql_command)
        except Exception as e:
            logger.error("Execute command to database failed, {}".format(e))

    @staticmethod
    def execute_file(cursor, sql_file):
        result = []

        file = open(sql_file, 'r')
        sql_text = file.read()
        file.close()

        try:
            for command in sql_text.split(';'):
                if command == '' or command == '--': continue
                cursor.execute(command)
                result.append({"query": command, "result": cursor.fetchall()})
        except Exception as e:
            logger.error("Execute file to database failed, {}".format(e))
        return result

    @staticmethod
    def insert_data(cursor, table_name, source):
        for item in source:
            column_names = ", ".join(item.keys())
            values = ', '.join("'{}'".format(i) for i in item.values())
            try:
                cursor.execute(DatabaseUtils.QUERY_INSERT_INTO.format(table_name, column_names, values))
            except Exception as e:
                logger.error("Insert data to database failed, {}".format(e))
