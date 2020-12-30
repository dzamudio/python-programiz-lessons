import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")

import inspect
import pprint
########################## HEADER ##########################


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])
        
Shape = Polygon(3)
Shape.inputSides()
Shape.dispSides()

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3) # super().__init__(3) is equivalent and preferred
    
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triange is %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

DZ.line("isinstance() checks if an object is an instance of another object of(Triangle, Polygon, int, object)")
DZ.line(isinstance(t,Triangle))
DZ.line(isinstance(t,Polygon))
DZ.line(isinstance(t,int))
DZ.line(isinstance(t,object))

DZ.line("issubclass() checks for class inheritance from (Triangle, Polygon, int)")
DZ.line(issubclass(Polygon,Triangle))
DZ.line(issubclass(Triangle,Polygon))
DZ.line(issubclass(bool,int))