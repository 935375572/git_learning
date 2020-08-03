"""
删除元素
"""

names = ["zhangsan","lisi","wangwu"]

# 1 使用del关键字 永久删除索引
del names[0]
print(names)

names = ["zhangsan","lisi","wangwu"]
# 2 删除第一个元素并且把zhangsan这个值存储到  huha
huha = names.pop(0)
print(names)
print(huha)

names = ["zhangsan","lisi","wangwu"]
# 3 也可以不指定索引。删除最后一个元素存储到变量 huha 中去
huha = names.pop()
print(names)
print(huha)

# 4 根据值来删除元素 remove方法
names = ["zhangsan","lisi","wangwu"]
# remove 也可以继续使用它的值  先将值存储到变量zhangsan中
zhangsan = "zhangsan"
names.remove(zhangsan)
print(zhangsan)
print(names)

# 5 根据值来删除元素 remove方法，使用while循环来解决重复值得问题
names = ["zhangsan","lisi","wangwu","zhangsan"]
print(names)

while names:
    if "zhangsan" in names:
        names.remove("zhangsan")
        print(names)