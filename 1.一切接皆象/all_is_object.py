def prin_name(name='nobody'):
    print(name)


class Person:
    def __init__(self):
        print('nobody-2')


my_func = prin_name
my_func('张三')

my_class = Person
my_class()

# 还可以将对象传递给集合对象中
obj_list = []

obj_list.append(prin_name)
obj_list.append(Person)

for item in obj_list:
    print(item())


# 将函数当成返回值
def decorator_func():
    print('start...')
    return prin_name


# 装饰器的用法
my_func_return = decorator_func()
my_func_return('李四')


# 将函数作为参数传递给另外一个函数

def a():
    print(1)


def b(func):
    return func


c = b(a)
c()
