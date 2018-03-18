class Animal(object):
    def __init__(self, name):
        self._name = name.lower().capitalize()
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value
    def make_sound(self):
        pass





class Dog(Animal):
#    def __init__(self, name):
#        self._name = name.lower().capitalize()
#    def get_name(self):
#        return self._name
#    def set_name(self, value):
#        self._name = value
#    def bark(self):
#        print(self.get_name() + ' is making sound wang wang wang...')
    def make_sound(self):
        print(self.get_name() + ' is making sound wang wang wang...')


class Cat(Animal):
#    def __init__(self, name):
#        self._name = name
#    def get_name(self):
#        return self._name
#    def set_name(self, value):
#        self._name = value
    def make_sound(self):
        print(self.get_name() + ' is making sound miu miu miu...')

class Snake(object):
    def __init__(self, name):
        self._name = name.lower().capitalize()
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value.lower().capitalize()
    def si(self):
        print(self.get_name() + ' is making sound si si si...')


WangCai = Dog('wangcai')
Kitty = Cat('kitty')
#WangCai.bark()
WangCai.make_sound()
#Kitty.mew()

Python = Snake('python')
Python.si()


print(WangCai)
print(Kitty)
print(Python)





animals = [Dog('wangcai'),Dog('laifu'),Cat('g-Green')]
for animal in animals:
    animal.make_sound()
