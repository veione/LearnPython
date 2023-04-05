class Student:
    def __init__(self, student_list):
        self.student = student_list

    # 魔法函数
    def __getitem__(self, item):
        return self.student[item]

    def __len__(self):
        return len(self.student)


student = Student(['张三', '李四', '王五', '赵六'])

print(type(student))
stu = student[:2]
print(type(stu))
print(len(stu))
print(len(student))

for item in student:
    print(item)

'''
魔术方法是Python定义的方法
魔术方法的名称不能随意更改
对当前这个类进行了功能扩展

item 索引 index

从0开始
直到Python运行抛出异常，自动结束for循环

魔法方法可以更改当前这个类的类型

如果要对一个对象进行迭代的话，对象一定是一个迭代器
'''
