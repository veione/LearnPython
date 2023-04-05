import sys

age = 22  # 整数型，可以通过print(sys.maxsize)查看最大值取值范围
print(age)  # 输出：22
print(sys.maxsize)

weight = 116.65  # 浮点型
print(weight)  # 输出：116.65

c1 = 1 + 2j
c2 = 2 + 3j
print(c1 + c2)  # 输出：(3+5j)，复数在实际工作中几乎用不到
print(complex(2, 1))  # 输出：(2+1j)

print(True == 1)  # 输出：True
print(False == 0)  # 输出：True
# True==1,False==0，因此True和False可以和数字相加
print(True + 1)  # 输出：2
print(False - 2)  # 输出：-2

# 其实布尔类型就是整数型的子类，可以使用内置函数issubclass()判断，该函数用于判断一个类型对象是否是另外一个类型对象的子类
print(issubclass(bool, int))  # 输出：True

# 字符串类型
# 字符串必须使用 '' 或者 "" 括起来，对于特殊字符可以使用反斜杠和 \ 进行转义，用 + 拼接多个字符串
# 用 * 复制字符串，字符串还支持索引截取（又叫切片）
name = "ZhangSan"  # 字符串类型，也可以使用单括号
print(name)  # 输出：ZhangSan
print(name * 2)  # 输出字符串两次，也可以写成 print(2 * name)，输出：ZhangSanZhangSan
print(name + '-123')  # 拼接字符串，输出：ZhangSan-123
print(name + '\'123\'')  # 拼接字符串并将单引号转义，输出：ZhangSan'123'

print(name[0:-1])  # 输出第一个至倒数第二个的字符，截取时顾头不顾尾，输出：ZhangSa
print(name[0])  # 输出第一个字符，输出：Z
print(name[-1])  # 输出最后一个字符，输出：n
print(name[2:])  # 输出从第三个开始之后的所有字符，输出：angSan
print(name[0:-1:2])  # 输出第一个至倒数第二个的字符，步长为2，输出：Zaga
# print(name[8])  # 若字符不存在，则会抛出IndexError: string index out of range

# 列表
# 列表是一组可重复有序的数据集合，任何类型的数据都可以存到列表中，会根据需要动态分配和回收内存，是Python
# 中使用最频繁的数据类型，列表同样也支持索引截取（切片），列表中的元素是可变的，能够进行增删改查操作

list_1 = []  # 创建一个空列表
list_2 = ['张三', 'lisi', 20, 3.1415926, '赵公子']  # 直接使用中括号创建列表
list_3 = list(['lisi', 12, (90, 28, 57), '吴承恩'])  # 或者调用内置list()函数，通常用于转换为列表时使用
print(list_1)  # 输出：[]
print(list_2)  # 输出：['张三', 'lisi', 20, 3.1415926, '赵公子']
print(list_3)  # 输出：['lisi', 12, (90, 28, 57), '吴承恩']

# 获取列表中的元素
print(list_2[1])  # 获取列表l1中第二个元素，输出：lisi
print(list_2[0:2])  # 获取列表l1中第一个和第二个元素，输出：['张三', 'lisi']
print(list_2[-5:-2])  # 获取列表l1中第一个至倒数第三个数据，反向索引，输出：['张三', 'lisi', 20]
print(list_2[2:-1])  # 获取列表l1中第三个至倒数第二个元素，输出：[20, 3.1415926]
print(list_2[1::2])  # 获取列表l1中第二个至最后一个元素，步长为2，输出：['lisi', 3.1415926]
print(list_2[:1:-2])  # 反向获取列表l1中元素，步长为-2，输出：['赵公子', 20]
print(list_2[::-1])  # 步长为-1时表示倒序排列元素，输出：['赵公子', 3.1415926, 20, 'lisi', '张三']
print(list_3[2][0])  # 获取l3嵌套列表(即第四个元素)中的第一个元素，输出：90
print(list_3[2][-1])  # 获取l3嵌套列表(即第四个元素)中的最后一个元素，输出：57
# print(list_2[5])  # 若元素不存在，则会抛出IndexError: list index out of range

for i in list_2:  # 使用for循环遍历列表中的元素
    print(i)  # 遍历元素后的操作，比如输出结果

# 列表排序
li = [1, 9, 10, 8, 6, 5, 0, 7, 3, 2]  # 对于需要排序的列表，元素类型必须一致，比如：元素统一为数字或者字符串
li.sort()
print(li)  # 输出：[0, 1, 2, 3, 5, 6, 7, 8, 9, 10]
li.sort(reverse=True)  # 指定reverse=True后列表会进行降序排列
# 还可以调用内置函数sorted()进行排序，此方式不会改变原列表
sorted(li)
sorted(li, reverse=True)  # 同样指定reverse=True后列表会进行降序排列
print(li)  # 输出：[10, 9, 8, 7, 6, 5, 3, 2, 1, 0]

# 修改列表中的元素
li[1] = '李四'
print(li)  # 输出：[10, '李四', 8, 7, 6, 5, 3, 2, 1, 0]
li[1:3] = ['张三', '李四']  # 输出：[10, '张三', '李四', 7, 6, 5, 3, 2, 1, 0]
print(li)

# 列表中添加元素
l1 = [1, 2, 3]
l1.append(4)
l2 = [4, 5, 6]
l2.append(6)
l3 = l1 + l2
print(l3)  # 输出：[1, 2, 3, 4, 4, 5, 6, 6]
l2.extend('3M')
l2.extend('HuaWei')
print(l2)  # [4, 5, 6, 6, '3', 'M', 'H', 'u', 'a', 'W', 'e', 'i']

l2.insert(1, '王德发')
l2.insert(0, 14)
print(l2)  # [14, 4, '王德发', 5, 6, 6, '3', 'M', 'H', 'u', 'a', 'W', 'e', 'i']

# append()、extend()、insert()三者区别:
# append()：指在列表的末尾田添加一个元素，新元素会视为一个整体追加到列表末尾
# extend()：指在列表的末尾至少添加一个元素，新元素会将整体中的每一个元素一个个地追加到列表末尾
# insert()：指在列表的指定索引位置添加元素

# 删除元素
l2.remove('王德发')  # 删除指定元素，一次只能删除一个元素，若出现重复的元素则只删除第一个
# l2.remove('no_data') #删除不存在的元素，会抛出ValueError：list.remove(x)：x not in list
l2.pop(1)  # 删除指定索引位置上的元素，若不指定索引则默认删除最后一个元素
l2.pop(8)  # 若索引不存在则抛出IndexError: pop index out of range
l2.clear()  # 清空列表
del l2  # 删除列表

# 元组
# 元组也是一组可重复且有序的对象集合，任何类型的数据都可以存到元组中，但是元组的元素是不可变的，元组同样也支持索引截取（切片）

# 创建元组
t0 = ()  # 创建空元组
t1 = ('张三', '李四', '王五', ['peter', 'jane', 'sam', 'allen'])  # 直接使用小括号创建元组
t2 = (1,)  # 当元组只有一个元素时需要在后面加上逗号
t3 = tuple(('allen', 'james', 'gallery'))  # 或者调用内置函数tuple()，通常用于转换为元组时使用

print(t1[1])
print(t1[0:2:2])
print(t1[0:-1])
for t in t1:
    print(t)
print(t1 + t2)  # 拼接元组

# 字典
# 字典是一组可变的无序的对象集合，字典中的元素是通过键(Key）：值(Value)来保存的，一组键值对称为一个元素，
# 其中键不可重复，必须唯一，而值是可重复的，字典会浪费较大的内存，是一种使用空间换时间的数据类型

# 创建字典
d0 = {}  # 创建一个空字典
d1 = {'name': '张三', 'age': 18, 'height': 175}  # 使用花括号创建字典
d2 = dict(name='李四', age=22, height=182)  # 使用内置函数dict()创建，通常用于转换字典时使用

print(d1["name"])  # 使用中括号根据Key获取Value值，输出：张三
# print(d1["张三"])  # 若Key不存在，则抛出KeyError: '张三'

# ↓还可以使用get()方法取值，此方式若Key不存在则返回None，不会抛出KeyError异常，还可以设置默认Value
print(d1.get("name"))  # 使用get()方法取值，输出：张三
print(d1.get("weight", 98))  # 若对应Key不存在则输出默认值，否则输出对应的Value值，此处输出：98

# ↓使用keys()方法获取所有Key
print(d1.keys())  # 获取字典中所有的Key，输出：dict_keys(['name', 'age', 'height'])
print(list(d1.keys()))  # 获取字典中所有的Key并转为列表，输出：['name', 'age', 'height']
print(tuple(d1.keys()))  # 获取字典中所有的Key并转为元组，输出：('name', 'age', 'height')

# ↓使用values()方法获取所有Value值
print(d1.values())  # 获取字典中所有的Value值，输出：dict_values(['张三', 18, 175])
print(list(d1.values()))  # 获取字典中所有的Value值并转为列表，输出：['张三', 18, 175]
print(tuple(d1.values()))  # 获取字典中所有的Value值并转为元组，输出：('张三', 18, 175)

# ↓使用items()方法获取所有的键值对
print(d1.items())  # 获取字典中所有的Key:Value，输出：dict_items([('name', '张三'), ('age', 18), ('height', 175)])
print(list(d1.items()))  # 获取字典中所有的Key:Value并转为列表，输出：[('name', '张三'), ('age', 18), ('height', 175)]
print(tuple(d1.items()))  # 获取字典中所有的Key:Value并转为元组，输出：(('name', '张三'), ('age', 18), ('height', 175))

for item in d1:  # 使用for循环遍历字典中的元素
    print(item)  # 返回字典中所有的Key

# 判断字典中是否存在指定的key
print('name' in d1)  # 判断d1字典中是否存在key 'name', 输出：True
print('age' not in d1)  # 判断d1字典中不存在key 'weight',输出：False

# 字典中元素的增删改
d1['name'] = '王五'  # 若key存在，则修改对应的Value值，原name对应的Value值变为王五
d1['weight'] = 98  # 若key不存在，则新增键值对，字典中新增'weight': 98
d1.pop('age')  # 删除key为'age'的键值对
d1.pop('name')  # 删除key为'name'的键值对
print(d1)

d1.setdefault('name', 'peter')  # 如果指定的key不存在则设置指定的键值对，如果存在则不受影响
d1.setdefault('name', '王五')  # 存在了则不进行操作
print(d1)
del d1['height']  # 同样也是删除key为'height'的键值对
d1.clear()  # 清空字典
del d1  # 删除字典,后面该符号不可则使用，否则会抛出：NameError: name 'd1' is not defined

# 集合
# 集合是一组可变的、无序的且不可重复的元素序列，可以理解为是没有Value值的字典，基本功能是测试元素之间的关系和删除重复元素，
# 比如：共同好友、你可能认识的人、关注TA的人还关注了。。。等
# 创建集合
s0 = set()  # 创建空集合，不能直接使用花括号，花括号默认是创建字典
s1 = {"张三", "李四", "王五", "赵六"}  # 花括号中元素非键值对时，创建的是集合
s2 = set("Allen")  # 调用内部函数set()创建，通常用于转换为集合时使用

# 获取集合中的元素
print(s1)
for i in s1:
    print(i)
ls = list(s1)  # 将集合转换为列表
print(ls[1])  # 获取列表中第二个元素，输出：李四
print(ls[0:2])  # 获取列表中第一个和第二个元素，输出：['张三', '李四']

# 判断元素是否存在
print('张三' in s1)  # 判断s1集合中是否存在'张三', 输出：True
print('李四' not in s1)  # 判断s1集合中是否不存在'李四',输出: False

# 集合中添加、更新元素
s1.add('周七')  # 添加一个元素，因为集合时无序的，所以元素位置随机
# update也可以理解为新增，当存在相同元素时，相同元素会被覆盖，不同元素会新增到集合中
s1.update('张三')  # 集合中会添加两个元素，'张', '三'
s1.update('张三丰')  # 集合中会更新两个元素,'张','三',新增一个元素'丰'
print(s1)

# 判断两个元素是否相等
print(s1 == s2)  # 输出：False
print(s1 != s2)  # 输出：True

# 判断两个集合的关系
s3 = {"李思", "张珊", "李思", "王武", "Andy"}
s4 = {"李四", "张珊", "张三", "王武"}
s5 = {"Andy"}

# ↓当s5中所有的元素s3里都有，但s5中的元素s3中未必有，则s3就是s5的超级，反之s5就是s3子集
print(s3.issuperset(s5))  # 判断s3是否是s5的超集，输出：True，因为s3中有s5所有的元素
print(s5.issubset(s3))  # 判断s5是否是s3的子集，输出：True，因为s5中的所有元素s3中都有
print(s3.isdisjoint(s4))  # 判断s3和s4两个集合是否没有交集，输出：False，因为两个集合中都有"张珊"和"王武"，存在交集

print(s3.intersection(s4))  # 输出s3和s4交集(即二者都有)的元素，输出：{'张珊', '王武'}
print(s3 & s4)  # 与intersection()等价，交集的一种符号表示法

print(s3.union(s4))  # 输出s3和s4并集(即去掉二者都有)的元素，输出：{'李思', '张三', '王武', '李四', '张珊', 'Andy'}
print(s3 | s4)  # 与union()等价，并集的一种符号表示法

print(s3.difference(s4))  # 输出s3和s4差集(即所有属于s3但不属于s4)的元素，输出：{'Andy', '李思'}
print(s3 - s4)  # 与union()等价，差集的一种符号表示法

print(s3.symmetric_difference(s4))  # 输出s3和s4对称差集(即s3中不属于s4和s4中不属于s3)的元素，输出：{'Andy', '李思', '李四', '张三'}
print(s3 ^ s4)  # 与symmetric_difference()等价，对称差集的一种符号表示法
