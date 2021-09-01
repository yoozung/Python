class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def printPoint(self):
        print('좌표:', self.x, self.y)

if __name__ == '__main__':
    points = []
    points.append(Point(1, 2))
    points.append(Point(3, 4))
    points.append(Point(5, 6))
    points.append(Point(7, 8))

    for p in points:
        p.printPoint()