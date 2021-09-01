'''
1.추가 2.검색 3.수정 4.삭제 5.전체출력
addr = []


추가함수
한 사람의 정보 입력받아 딕셔너리로 생성하여 리스트에 추가
{'name':'aaa', 'tel':'111', 'addr':'asdf'}


검색함수
검색할 이름 입력받음
addr 각 방의 name키값 비교 있나 없나 검색
있으면 출력 없으면 'not found'


수정함수
수정할 사람의 이름과 새 전화번호, 새 주소를 입력받아서
수정할 사람 이름으로 검색한 후 있으면 새 딕셔너리로 교체.


삭제함수
삭제할 사람의 이름 입력받아 검색해서 있으면
그 칸 삭제


전체출력함수
addr 전체 내용 출력
'''

list = []

#추가
def add_addr():
    global list
    for i in range(0, 3):
        item = {}
        val1 = input('이름 : ')
        item['name'] = val1

        val2 = input('전화번호 : ')
        item['tel'] = val2

        val3 = input('주소 : ')
        item['addr'] = val3
        list.append(item)

        print(list)

#검색
def find_addr():
    global list
    search = input('이름 : ')
    for i in range(len(list)):
        if list[i]['name'] != search:
            print('not found')
        else:
            print('found : ', search)

# 수정
def update_addr():
    global list
    name = input('변경할 사람의 이름 : ')
    for i in range(len(list)):
        if list[i]['name'] == name:
            tel = input('변경 전화번호 : ')
            addr = input('변경 주소 : ')
            list[i]['name'] = name
            list[i]['addr'] = addr
            print('변경후 : ', list[i])
        else:
            print('없는 사람입니다.')

# 삭제함수
def delete_addr():
    global list
    name = input('삭제할 사람의 이름 : ')
    for i in range(len(list)):
        if list[i]['name'] == name:
            del list[i]
            print('삭제 후 list', list)
        else:
            print('없는 사람입니다.')

# 전체출력
def all_addr():
    global list
    print(list)

def menu():
    while True:
        mm = input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료')
        if mm=='1':
            add_addr()
        elif mm=='2':
            find_addr()
        elif mm=='3':
            update_addr()
        elif mm=='4':
            delete_addr()
        elif mm=='5':
            all_addr()
        elif mm=='6':
            break

#############################################################
#members = [{'name':'aaa', 'tel':'1234', 'addr':'가나다라'}, {'name':'aaa', 'tel':'1234', 'addr':'가나다라'}] #주소들 저장할 리스트
members = []
keys = ['name', 'tel', 'addr'] #딕셔너리에서 사용할 키값

#주소 추가
def addAddr():
    mem = {}
    for i in keys:
        mem[i] = input(i+':')
        #이름 중복체크
        while i == 'name':
            d = getMember(mem[i])
            if d == None: #검색된 것이 없다. 중복안됨
                break
            else:
                print('중복된 이름. 다시 입력하세요')
                mem[i] = input(i + ':')
    members.append(mem)

def printMem(mem): #mem:{'name':'aaa', 'tel':'1234', 'addr':'가나다라'}
    for i in mem:
        print(i,':',mem[i])

    print('==============')

def printAll():
    for m in members:
        printMem(m)

def getMember(name): #파이썬은 리턴값이 없으면 None이 반환됨
    for m in members:
        if name == m['name']:
            return m

def searchMember():
    name = input('검색할 사람의 이름 : ')
    mem = getMember(name)
    if mem == None:
        print('없는 사람')
    else:
        printMem(mem)

def editMember():
    name = input('수정할 사람의 이름:')
    mem = getMember(name)
    if mem == None:
        print('없는 사람')
    else:
        for i in range(1, 3):
            mem[keys[1]] = input('new ' + keys[i] + ': ')

def delMember():
    name = input('삭제할 사람의 이름:')
    mem = getMember(name)
    if mem == None:
        print('없는 사람')
    else:
        members.remove(mem)

def menu():
    while True:
        mm = input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료')
        if mm=='1':
            addAddr()
        elif mm=='2':
            searchMember()
        elif mm=='3':
            editMember()
        elif mm=='4':
            delMember()
        elif mm=='5':
            printAll()
        elif mm=='6':
            break

if __name__ == '__main__':
    menu()