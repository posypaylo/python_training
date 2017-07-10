from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="root")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass   #  db.destroy()


# import mysql.connector
#
#
# connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="root")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for raw in cursor.fetchall():
#         print(raw)
# finally:
#     connection.close()


# from fixture.db import DbFixture
#
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="root")
#
# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()


