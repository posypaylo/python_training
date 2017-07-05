import mysql.connector


connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="root")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for raw in cursor.fetchall():
        print(raw)
finally:
    connection.close()