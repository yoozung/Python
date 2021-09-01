'''
입출력
입력: 데이터가 외부에서 프로그램 방향으로 흘러 들어감
출력: 데이터가 프로그램에서 외부로 흘러나감

1. 표준입출력(stdio)
기본 제공 입출력
sys.stdin: 표준입력(키보드 입력)
sys.stdout: 표준출력(콘솔출력)
sys.stderr: 표준에러(콘솔에러출력)
'''
import sys

sysin = sys.stdin   #표준입력 => reda(읽을 바이트수 지정)
sysout = sys.stdout #표준출력 => write(출력내용) => 반환값은 정상출력 문자 수

num = sysout.write('글자를 입력하시오\n')
sysout.write('출력한 글자 수: ' + str(num))
data = sysin.read(5)
sysout.write('5개만 읽음: ' + data+'\n')
sysin.readline() #버퍼에 남은 데이터 제거
x = sysin.readline()    #새롭게 한 줄 입력
sysout.write('나머지 데이터: ' + x)

