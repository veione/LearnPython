"""
JAVA
    不支持多继承

抽象类
1.不能被实例化
2.可以继承
3.继承抽象类之后必须重载抽象类的方法
    重写

Python
    抽象类的概念

1.类型判断
2.对于类进行方法的限制
"""
import abc
from abc import ABC


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


# 要求程序员知道当前这个类实现了__len__
com = Company(['张三', '李四'])
print(hasattr(com, '__len__'))

from collections.abc import Sized

print(isinstance(com, Sized))

'''
抽象基类不能被实例化
继承抽象类必须重载内部方法
'''


# s = Sized() #TypeError: Can't instantiate abstract class Sized with abstract methods __len__

class Test(Sized):

    def __len__(self):
        return 0


test = Test()

# 场景二
'''
我们去实现某个类的时候，必须要实现制定的方法

框架中比较多
web框架 Django

Django 框架中实现了缓存功能组件

redis
cache
memorycache

方法调用统一
    因为现在不确定用户使用的是Redis缓存还是文件缓存
    必须要让用户手动选择
    Redis设置缓存和文件设置缓存API接口必须一致
'''

# class CacheBase(metaclass=abc.ABCMeta):
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
#
# class RedisCache(CacheBase):
#     pass
#
#
# redis_cache = RedisCache()
# redis_cache.set('name', '张三')

# 导入Python全局的抽象基类
import abc


# 限制使用者必须按照规则使用内置的接口 API
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase, ABC):
    def __init__(self):
        self.dict = {}

    def get(self, key):
        return self.dict[key]

    def set(self, key, value):
        self.dict[key] = value


redis_cache = RedisCache()
redis_cache.set('name', '张三')
print(redis_cache.get('name'))

"""
尽量不去使用抽象基类
    利用了多继承
    mixin
    
造成约束限制不符合编程逻辑
"""
