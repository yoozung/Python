class Car:
    def horn(self):
        print('빵빵')

class 엠뷸런스(Car):
    def horn(self):
        print('삐뽀삐뽀')

class 소방차(Car):
    def horn(self):
        print('에~~엥')

class 불도저(Car):
    def horn(self):
        print('땅파땅파')

if __name__ == '__main__':

    while True:
        obj = None
        sel = input('1.엠뷸런드 2.소방차 3.불도저 4.종료')
        if sel == '1':
            obj = 엠뷸런스()
        elif sel == '2':
            obj = 소방차()
        elif sel == '3':
            obj = 불도저()
        elif sel == '4':
            break

        if obj is not None:
            obj.horn()


