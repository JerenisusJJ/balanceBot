import sqlite3


def getTableInfo(provider_name):
    try:
        sqlite_connection = sqlite3.connect('balance.db')
        cursor = sqlite_connection.cursor()
        #print("get_table_info Подключен к SQLite")
        sql_select_query = """select provider_balance from providerdata where provider_name = ? """  # """select provider_balance from providerdata where provider_name = ?"""
        cursor.execute(sql_select_query, (provider_name,))
        records = cursor.fetchone()
        balance = records[0]
        cursor.close()
        return balance

    except sqlite3.Error as error:
        print("get_table_info Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            #print("get_table_info Соединение с SQLite закрыто")


def updateTableInfo(provider_name, provider_balance):
    try:
        sqliteConnection = sqlite3.connect('balance.db')
        cursor = sqliteConnection.cursor()
        #print("updateSqliteTable Connected to SQLite")

        sql_update_query = """Update providerdata set provider_balance = ? where provider_name = ?"""
        data = (provider_balance, provider_name)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        #print("updateSqliteTable Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("updateSqliteTable The sqlite connection is closed")
