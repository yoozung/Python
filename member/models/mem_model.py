import cx_Oracle

class Member:
    def __init__(self, id=None, pwd=None, name=None, email=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

class Dao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        return self.conn.cursor()

    def insert(self, m:Member):
        cursor = self.connect()
        sql = 'insert into member values(:1, :2, :3, :4)'
        d = (m.id, m.pwd, m.name, m.email)
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def select(self, id:str) -> Member: #-> Member 이건 리턴타입을 나타내는 것
        cursor = self.connect()
        sql = 'select * from member where id=:1'
        d = (id, )
        cursor.execute(sql, d)
        row = cursor.fetchone()
        self.conn.close()
        if row is not None:
            return Member(row[0], row[1], row[2], row[3])

    def selectAll(self) -> list:
        members = []
        cursor = self.connect()
        sql = 'select * from member'
        cursor.execute(sql)
        for row in cursor:
            members.append(Member(row[0], row[1], row[2], row[3]))
        self.conn.close()
        return members

    def update(self, m:Member):
        cursor = self.connect()
        sql = 'update member set pwd=:1 where id=:2'
        d = (m.pwd, m.id)
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def delete(self, id:str):
        cursor = self.connect()
        sql = 'delete member where id=:1'
        d = (id, )
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

class Service:
    def __init__(self):
        self.dao = Dao()

    def addMember(self, m:Member):
        self.dao.insert(m)

    def getMember(self, id):
        return self.dao.select(id)

    def getAll(self):
        return self.dao.selectAll()

    def editMember(self, m:Member):
        self.dao.update(m)

    def delMember(self, id:str):
        self.dao.delete(id)


