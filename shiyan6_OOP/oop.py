#!/usr/bin/env python3

class Animal(object):
    owner = 'ming'
    def __init__(self, name):
        self._name = name.lower().capitalize()
    @classmethod
    def get_owner(cls):
        return cls.owner
    @staticmethod
    def order_animal_food():
        print('ording...')
        print('ok')
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value
    def make_sound(self):
        pass

Animal.order_animal_food()


class Animal_II:
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError

    



cat_II = Animal_II()
#cat_II.age = 'h'
cat_II.age = 2
print(cat_II.age)

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





class Shiyanlou:
    __private_name = 'shiyanlou'
    def __get_private_name(self):
        return self.__private_name

s = Shiyanlou()
#print(s.__private_name)
print(s._Shiyanlou__private_name)
print(s._Shiyanlou__get_private_name())
print(Animal.owner)
print(WangCai.owner)


print(Animal.get_owner())
print(Kitty.get_owner())
