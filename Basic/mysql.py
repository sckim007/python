import pymysql.cursors

'''
Check connection
'''
def check_connection():

'''
데이터베이스 생성
'''
'''
conn = pymysql.connect(host='localhost',
                       user='sckim007',
                       password='kscksc7315',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'CREATE DATABASE test1'
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()
'''

'''
테이블 생성
'''
'''
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='sckim007',
                       password='kscksc7315',
                       db='test1',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = """
            CREATE TABLE users (
                id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name varchar(255) NOT NULL,
                phone_number varchar(255) NOT NULL,
                e_mail varchar(255) NOT NULL,
                address varchar(255) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8
            """
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()
'''

'''
레코드 삽입
'''
"""
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='sckim007',
                       password='kscksc7315',
                       db='test1',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO users (name, phone_number, e_mail, address) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, ('sckim', '010-1111-1111', 'sckim007@gmail.com', 'Dajeon'))
    conn.commit()
    print(cursor.lastrowid)
    # 1 (last insert id)
finally:
    conn.close()
"""

'''
데이터 조회
'''

import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='sckim007',
                       password='kscksc7315',
                       db='test1',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM users WHERE e_mail = %s'
        cursor.execute(sql, ('sckim007@etri.re.kr',))

        #result = cursor.fetchone()
        result = cursor.fetchall()
        print(result)
        # (1, 'test@test.com', 'my-passwd')
        
finally:
    conn.close()


'''
데이터갱신
'''
"""
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='sckim007',
                       password='kscksc7315',
                       db='test1',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'UPDATE users SET e_mail = %s WHERE e_mail = %s'
        cursor.execute(sql, ('sckim007@etri.re.kr', 'sckim007@etri.re.rk'))
    conn.commit()
    print(cursor.rowcount)  # 1 (affected rows)
finally:
    conn.close()
"""

'''
데이터 삭제
'''
"""
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='sckim007',
                       password='kscksc7315',
                       db='test1',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'DELETE FROM users WHERE e_mail = %s'
        cursor.execute(sql, ('sckim007@etri.re.kr',))
    conn.commit()
    print(cursor.rowcount)  # 1 (affected rows)
finally:
    conn.close()
"""
