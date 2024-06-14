class Shape:
    def __init__(self,length,breadth,radius):
        self.length=length
        self.breadth= breadth
        self.radius=radius
    # def area(self,length,breadth)

class Rectangle(Shape):
    def __init__(self, length, breadth, radius):
        super().__init__(length, breadth)
    def rect_area(self,length,breadth):
        self.area= self.length*self.breadth
    
class Circle(Shape):
    def __init__(self, length, breadth, radius): 
        super().__init__(radius)

    def circle_area(self,radius):
        self.area= 3.14* self.radius **2

Circle1=Circle(20)
Circle1.circle_area
print(Circle1.area)



