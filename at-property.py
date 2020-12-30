import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")
#import inspect
import pprint
#########################DZ.line("HEADER ##########################

# problem... refactoring a class that had getters/setters added...
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    # getter method
    def get_temperature(self):
        print("Getting value...")
        return self._temperature
    
    # setter method
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value
    
    # creating a property object
    temperature = property(get_temperature, set_temperature)
    # property(fget=None, fset=None, fdel=None, doc=None)
    # fget gets val of attr
    # fset sets val of attr
    # fdel deletes attr
    # doc is a string(comment)
    # You can manually set the methods for property later...
    # temperature = property()
    # temperature = temperature.getter(get_temperature)
    # temperature = temperature.setter(set_temperature)
    # eq ^^^
    DZ.line("CONTINUE TO: https://www.programiz.com/python-programming/property")

# to this will be a nightmare... right
human = Celsius(37)
print(human.get_temperature())
print(human.to_fahrenheit())
human.set_temperature(-30)
print(human.to_fahrenheit())

DZ.line("Old code to refactor")
### OLD CODE BEGIN ###
human2 = Celsius()
human2.temperature = 0
print(human2.temperature)
print(human2.to_fahrenheit())
### OLD CODE END ###