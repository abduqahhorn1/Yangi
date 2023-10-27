class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rect(5, 7)

print(rectangle.area()) 