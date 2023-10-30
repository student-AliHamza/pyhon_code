
class rectangle:
    def __init__(self,width,hight):
        self.width = width
        self.hight = hight
    def area(self):
        return self.width * self.hight
    def perimeter(self):
        return 2*(self.width + self.hight)
    
my_rectangle = rectangle(5,10)

print("Area",my_rectangle.area())
print("perimeter",my_rectangle.perimeter())

