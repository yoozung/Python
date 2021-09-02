import cx_Oracle

class Member:
    def __init__(self, id=None, pwd=None, name=None, email=None):
        self.__id = id
        self.__pwd = pwd
        self.__name = name
        self.__email = email

    def __str__(self):
        return 'id: ' + self.__id + ' / pwd: ' + self.__pwd + ' / name: ' + self.__name + ' / email: ' + self.__email

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setPwd(self, pwd):
        self.__pwd = pwd

    def getPwd(self):
        return self.__pwd

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

class Dao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        return self.conn.cursor()

    def add(self, m):
        cursor = self.connect()
        sql = 'insert into member values(:0, :1, :2, :3)'
        d = (m.getId(), m.getPwd(), m.getName(), m.getEmail())
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def selectById(self, id):
        cursor = self.connect()
        sql = 'select * from where id=:1'
        d = (id,)
        cursor.excute(sql, d)
        row = cursor.fetchone()
        self.conn.close()
        if row is not None:
            return Member(row[0], row[1], row[2], row[3])

    def edit(self, m):
        cursor = self.connect()
        sql = 'update member set pwd=:1 where id=:2'
        d = (m.getPwd(), m.getId())
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def delete(self, id):
        cursor = self.connect()
        sql = 'delete member where id=:1'
        d = (id,)
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def all(self):
        res = []
        cursor = self.connect()
        sql = 'select * from member'
        cursor.execute(sql)
        for row in cursor:
            res.append(Member(row[0], row[1], row[2], row[3]))
        self.conn.close()
        return res

class Service:
    def __init__(self):
        self.__dao = Dao()

    def addMember(self, m):
        self.__dao.add(m)

    def getMemberById(self, id):
        return self.__dao.selectById(id)

    def editMember(self, m):
        self.__dao.edit(m)

    def delMember(self, id):
        self.__dao.delete(id)

    def printAll(self):
        return self.__dao.all()

