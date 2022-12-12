"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
import cx_Oracle as oci

# (0) 테이블 생성
def createDBTable():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
    sql = '''
        CREATE TABLE contact
        (
        name            varchar2(30),
        phone_number    varchar2(50),
        email           varchar2(60),
        addr            varchar2(200)
        )    
    '''
    cursor = conn.cursor()
    cursor.execute(sql)

    cursor.close()
    conn.close()

class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_number)
        print("이메일:", self.email)
        print("주소:", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = input('메뉴 선택: ')
    return int(menu)

def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    # Contact 객체를 생성하고 DB 에 입력
    name = input('이름은? ')
    phone_number = input('전화번호는? ')
    email = input('이메일은? ')
    addr = input('주소는? ')
    # record = Contact(name, phone_number, email, addr)
    data = [name, phone_number, email, addr]

    conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
    sql = '''
        INSERT INTO contact
        VALUES (:0, :1, :2, :3)
       '''
#    values = [record.name, record.phone_number, record.email, record.addr]
    cursor = conn.cursor()
    cursor.execute(sql, data)

    cursor.close()
    conn.commit()   # DDL이 아닌 경우 자동 commit이 안 된다
    conn.close()

def print_contact():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
    sql = '''
        SELECT * FROM contact
       '''

    cursor = conn.cursor()
    cursor.execute(sql)

    datas = cursor.fetchall()
    for row in datas:
        print('이름:', row[0], '전화번호:', row[1], '이메일:', row[2], '주소:',  row[3])

    cursor.close()
    conn.close()

def delete_contact(name):
    conn = oci.connect('scott/tiger@127.0.0.1:1521/orcl')
    sql = "DELETE FROM CONTACT WHERE NAME LIKE'" + name + "'"
    cursor = conn.cursor()
    cursor.execute(sql)

    cursor.close()
    conn.commit()  # DDL이 아닌 경우 자동 commit이 안 된다
    conn.close()

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
#    createDBTable()
     run()
