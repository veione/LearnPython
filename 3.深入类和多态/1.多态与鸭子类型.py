'''
多态：
    继承：多态一定是发生在子类和父类之间的
    重写：子类重新父类中的方法
'''


class Animal:
    def say(self):
        print('I am a animal')


class Cat(Animal):
    def say(self):
        print('I am a cat')


class Dog(Animal):
    def say(self):
        print('I am a dog')


class Duck(Animal):
    def say(self):
        print('I am a duck')


animal = Dog()
animal.say()

animal = Duck()
animal.say()

"""
鸭子类型：
    一种动物长得像鸭子，叫起来也像鸭子，那么这个动物就是一个鸭子

多个类中实现了同一个方法（当前方法的名称一样）
    方法名
    
    不关注方法的实现方式，只看当前这个方法的名称
    
Python 的关注点是当前这个对象的类型
"""


class Dog:
    def say(self):
        print('I am a dog')


class Cat:
    def say(self):
        print('I am a cat')


class Duck:
    def say(self):
        print('I am a duck')


animal = Dog
animal().say()

animal = Cat
animal().say()

animal_list = [Dog, Cat, Duck]
for animal in animal_list:
    animal().say()

# 关于鸭子类型的实现案例
list_a = [1, 2]
list_b = [3, 4]

list_a.extend(list_b)
print(list_a)

set_data = set()
set_data.add(5)
set_data.add(6)

list_a.extend(set_data)
print(list_a)

# list_a 是一个列表类型，那么为什么集合也可以进行追加
'''
extend 只要是迭代类型，就可以进行追加

list
set

    都是可迭代额
    
    __iter__
可迭代的类
'''