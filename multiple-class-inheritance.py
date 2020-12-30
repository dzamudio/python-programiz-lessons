import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")
#import inspect
import pprint
########################## HEADER ##########################


DZ.line("how to inherite from multiple classes into derived class")

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2): # Method Resolution Order(MRO): is [MultiDerived, Base1, Base2, object]
    pass


DZ.line("how to multilevel inherit")

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1): # MRO: is [Derived2, Derived1, Base, Object]
    pass


DZ.line("everything is a object")
DZ.line(issubclass(list,object))
DZ.line(isinstance(5.5,object))
DZ.line(isinstance("Hello",object))

DZ.line("Use __mro__ to dissect the MRO of a class")
print(MultiDerived.__mro__)
print(Derived2.__mro__)