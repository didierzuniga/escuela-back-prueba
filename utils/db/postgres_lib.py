#!/usr/bin/python
import psycopg2
import json
import os
 
def connect(param, *args, **kwargs):
    """ Conexión al servidor de base de datos PostgreSQL """
    connection = None
    try:
        print('Conectando a la base de datos PostgreSQL...')

        connection = psycopg2.connect(host=os.environ['DB_HOST'], database=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'])
        cur = connection.cursor()

        # |||||||||||||||  SIGNIN  |||||||||||||||||

        if param == 'signin':
            cur.execute('SELECT * FROM users')
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'id': i[0],
                    'username': i[1],
                    'firstname': i[2],
                    'lastname': i[3],
                    'profile': i[4],
                    'password': i[5]
                })
            return data



        # |||||||||||||||  ALL  |||||||||||||||||
        if param == 'allUsers':
            cur.execute('SELECT * FROM users')
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'username': i[1],
                    'firstname': i[2],
                    'lastname': i[3],
                    'profile': i[4]
                })
            return data

        if param == 'allCourses':
            cur.execute('SELECT co.name, us.firstname, us.lastname FROM courses AS co JOIN users AS us ON (us.id = co.id_teacher)')
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'name': i[0],
                    'teacher': i[1] + ' ' + i[2],
                })
            return data

        if param == 'allModules':
            cur.execute('SELECT name FROM modules')
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'name': i[0]
                })
            return data




        # |||||||||||||||  GET ONE  |||||||||||||||||
        if param == 'user':
            cur.execute('SELECT username, firstname, lastname, profile FROM users WHERE id={0}'.format(kwargs.get('id', None)))
            dt = cur.fetchall()
            data = {}
            for i in dt:
                data['username'] = i[0]
                data['firstname'] = i[1]
                data['lastname'] = i[2]
                data['profile'] = i[3]
            return data

        if param == 'course':
            cur.execute('SELECT co.name, us.firstname, us.lastname FROM courses AS co JOIN users AS us ON (us.id = co.id_teacher) WHERE co.id={0}'.format(kwargs.get('id', None)))
            dt = cur.fetchall()
            data = {}
            for i in dt:
                data['name'] = i[0]
                data['teacher'] = i[1] + ' ' + i[2]
            return data

        if param == 'module':
            cur.execute('SELECT name FROM modules WHERE id={0}'.format(kwargs.get('id', None)))
            dt = cur.fetchall()
            data = {}
            for i in dt:
                data['name'] = i[0]
            return data


        # |||||||||||||||  GET COURSE INFO  |||||||||||||||||
        # (SELECT mo.name, ml.score FROM modules_log AS ml JOIN modules AS mo ON (ml.id_module = mo.id) WHERE ml.id_course_log={0} as modules) 
        if param == 'courseInfo':
            cur.execute('SELECT us.id, cl.id_student, us.firstname, us.lastname, cl.score, cl.id FROM courses_log AS cl JOIN users AS us ON (us.id = cl.id_student) WHERE cl.id_course={0}'.format(kwargs.get('id', None)))
            dt = cur.fetchall()
            
            data = []
            for i in dt:
                data.append({
                    'id': i[0],
                    'id_student': i[1],
                    'fullname': i[2] + ' ' + i[3],
                    'score': i[4],
                    'courseLogId': i[5],
                })
            return data


        # |||||||||||||||  GET STUDENT COURSES  |||||||||||||||||
        if param == 'studentCourses':
            cur.execute('SELECT co.id, co.name, us.firstname, us.lastname, cl.score FROM courses_log AS cl JOIN users AS us ON (us.id = cl.id_student) JOIN courses AS co ON (co.id = cl.id_course) WHERE cl.id_student={0}'.format(kwargs.get('id', None)))
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'id': i[0],
                    'name': i[1],
                    'fullname': i[2] + ' ' + i[3],
                    'score': i[4]
                })
            return data

        # |||||||||||||||  GET TEACHER COURSES  |||||||||||||||||
        if param == 'teacherCourses':
            cur.execute('SELECT id, name FROM courses WHERE id_teacher={0}'.format(kwargs.get('id', None)))
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'id': i[0],
                    'name': i[1],
                })
            return data
        
        # |||||||||||||||  GET STUDENT MODULES  |||||||||||||||||√√√
        if param == 'studentModules':
            cur.execute('SELECT mo.name, ml.score FROM modules AS mo JOIN modules_log AS ml ON (mo.id = ml.id_module) JOIN courses_log AS cl ON (cl.id = ml.id_course_log) WHERE cl.id_course={0} AND cl.id_student={1}'.format(kwargs.get('courseId', None), kwargs.get('studentId', None)))
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'name': i[0],
                    'score': i[1]
                })
            return data

        # |||||||||||||||  GET STUDENT MODULES FOR TEACHER |||||||||||||||||√√√
        if param == 'studentModulesForTeacher':
            cur.execute('SELECT ml.id, mo.name, ml.score, us.firstname, us.lastname FROM modules_log AS ml JOIN modules AS mo ON (mo.id = ml.id_module) JOIN courses_log AS cl ON (cl.id = ml.id_course_log) JOIN users AS us ON (us.id = cl.id_student) WHERE ml.id_course_log={0}'.format(kwargs.get('courseLogId', None)))
            dt = cur.fetchall()
            data = []
            for i in dt:
                data.append({
                    'id': i[0],
                    'name': i[1],
                    'score': i[2],
                    'student_name': i[3] + ' ' + i[4]
                })
            return data

        # |||||||||||||||  UPDATE STUDENT MODULE  |||||||||||||||||√√√
        if param == 'updateStudentModule':
            sql_update_query = """UPDATE modules_log SET score = %s where id = %s"""
            cur.execute(sql_update_query, (kwargs.get('score', None), kwargs.get('moduleLogId')))
            connection.commit()
            return cur.rowcount


        connection.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Conexión finalizada.')
 
 
if __name__ == '__main__':
    connect()
