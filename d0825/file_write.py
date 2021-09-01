def file_write(fname):
    f1 = open(fname, 'w', encoding='utf-8')
    while True:
        data = input('메세지 입력. 멈추려면 /stop 입력')
        if data == '/stop':
            break
        f1.write(data + '\n')
    f1.close()

# 파일복사하는 함수를 만드시오
# 파라메터: 원본파일명, 타깃파일명
def file_read(fname):
    f = open(fname, 'r', encoding='utf-8')
    msg = f.read()
    f.close()
    return msg

#파일쓰기 함수. fname은 쓰기 할 파일 경로. msg는 파일에 쓸 내용
def file_write2(fname, msg):
    f = open(fname, 'w', encoding='utf-8')
    f.write(msg)
    f.close()

def file_copy(fname1, fname2):
    msg = file_read(fname1)
    file_write2(fname2, msg)
    print('복사완료')

# 파일 읽기 함수(파일명)

if __name__ == '__main__':
    file_copy('files/a.txt', 'files/c.txt')
    msg = file_read('files/c.txt')
    print('##복사된 내용: ')
    print(msg)