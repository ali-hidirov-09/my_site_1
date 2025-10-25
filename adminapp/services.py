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
        cursor.execute("""
            SELECT k.id, k.name, f.name AS faculty_name
            FROM adminapp_kafedra AS k
            LEFT JOIN adminapp_faculty AS f ON k.faculty_id = f.id
        """)
        kafedra = dict_fetchall(cursor)
        return kafedra


def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT s.id, s.name, k.name AS kafedra_name
        FROM adminapp_subject AS s
        LEFT JOIN adminapp_kafedra AS k ON s.kafedra_id = k.id
        """)
        subject = dict_fetchall(cursor)  # dictga o'tkazish
        return subject


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT 
                t.id,
                t.full_name,
                k.name AS kafedra_name,
                GROUP_CONCAT(s.name, ', ') AS subject_names
            FROM adminapp_teacher AS t
            LEFT JOIN adminapp_kafedra AS k ON t.kafedra_id = k.id
            LEFT JOIN adminapp_teacher_subjects AS ts ON t.id = ts.teacher_id
            LEFT JOIN adminapp_subject AS s ON ts.subject_id = s.id
            GROUP BY t.id, t.full_name, k.name
        """)
        return dict_fetchall(cursor)



def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT g.id, g.name, s.name AS subject_name
        FROM adminapp_group AS g
        LEFT JOIN adminapp_group_subject AS sg ON g.id = sg.group_id 
        LEFT JOIN adminapp_subject AS s ON sg.subject_id = s.id
        """)
        group = dict_fetchall(cursor)  # dictga o'tkazish
        return group


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT s.id, s.full_name, g.name AS group_name
        FROM adminapp_student AS s
        LEFT JOIN adminapp_group  AS g ON s.group_id = g.id""")
        student = dict_fetchall(cursor)  # dictga o'tkazish
        return student