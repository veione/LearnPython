"""
type class object 三者关系

type 可以创建一个类
class 声明一个类
object 所有类当中的基类

python中所有的类都是继承自object

type 可以创建类
类继承自 object

type 本身也是对象，只要是对象都继承自object

object是由type创建的，type又继承自object
二者是互补的关系

当type创建object的时候又继承了自己创建的object

type自身创建了自身

type可以创建Python中的对象，Python一切皆对象
type继承了object
object也是通过type创建的
type是由自身创建的

class 在Python中声明了一个类

type -> int -> obj


"""
a = 1
b = "abc"
print(type(1))
print(type(int))
print(type(b))
print(type(str))


class Student:
    pass


stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))
print(type(type))
