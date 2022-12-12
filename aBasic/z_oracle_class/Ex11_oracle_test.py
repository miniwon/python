# Ex11_oracle_test

import cx_Oracle as oci

# 1. 연결 객체 얻어 오기(Connection)
conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
print(conn.version)

# 2. sql 문장
sql = 'select * from emp'

# 3. cursor 객체 얻어 오기
cursor = conn.cursor()

# 4. 실행
cursor.execute(sql)

datas = cursor.fetchall()
# print(datas)
for row in datas:
    print(row[0], row[1], row[2])

# 5. cursor 객체 닫기
cursor.close()

# 6. 연결 객체 닫기
conn.close()
