# Ex12_oracle_csv.py

import cx_Oracle as oci
import csv

def createDBTable():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
    sql = '''
        CREATE TABLE supply
        (
        id              number          primary key,          
        Supplier_Name   varchar2(50),
        Invoice_Number  varchar2(50),
        Part_Number     varchar2(30),
        Cost            number,
        Purchase_Date   date
        )    
    '''
    cursor = conn.cursor()
    cursor.execute(sql)

    sql2 = 'create sequence seq_supply_id'
    cursor.execute(sql2)

    cursor.close()
    conn.close()

def saveDBTable(data):
    conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
    sql = '''
        INSERT INTO supply
        VALUES (seq_supply_id.NEXTVAL, :0, :1, :2, :3, :4)
       '''
    cursor = conn.cursor()
    cursor.execute(sql, data)

    cursor.close()
    conn.commit()   # DDL이 아닌 경우 자동 commit이 안 된다
    conn.close()

def viewDBTable(tableName):
    # 넘겨받은 테이블명의 데이터를 화면에 출력
    conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
    sql = '''
        SELECT * FROM
       ''' + tableName

    cursor = conn.cursor()
    cursor.execute(sql)

    datas = cursor.fetchall()
    for row in datas:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

    cursor.close()
    conn.close()

if __name__ == "__main__":
    # (1) 테이블 생성
    # createDBTable()

    # (2-0) 입력 확인
    # imsi = ['kosmo', '9999', '8888', 1000, '2022-12-24']
    #saveDBTable(imsi)

    # (2) 데이터 입력
    # file = open('supply.csv', 'r')
    # datas = csv.reader(file)

    # header = next(datas, None)  # None > 뭔가 수행할 게 없다?
    # print(header)
    # print('-'*100)
    #
    # for row in datas:
    #     #print(row)
    #     saveDBTable(row)

    # (3) 데이터 보기
    viewDBTable('supply')
