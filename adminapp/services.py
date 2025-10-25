from django.db import connection
from contextlib import closing

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_faculty""")
        faculties = dict_fetchall(cursor)  # dictga o'tkazish
        return faculties


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_kafedra""")
        kafedra = dict_fetchall(cursor)  # dictga o'tkazish
        return kafedra

