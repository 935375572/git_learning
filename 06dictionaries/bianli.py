"""
遍历所有的键值对  items()方法
"""
# 存储一组用户信息 用户名  姓 和 名
user_0 = {
    "user_name":"zhangsan",
    "first":"xiao",
    "last":"hh",
}

for key,value in user_0.items():  # 声明两个变量来存储键和值
    print("\nkey:" + key)
    print("value:" +value)

# 遍历所有的键 keys()方法   遍历字典时  会默认遍历所有的键。所以不用使用keys()方法也可以
for key in user_0.keys():
    print("key:" + key)


# 遍历字典中所有的值 方法values()
for value in user_0.values():
    print("value:" + value)

# 遍历值的时候 如果值出现重复，可以使用 集合 set 每个元素都是独一无二的
user_1 = {
    "user_name":"zhangsan",
    "first":"xiao",
    "last":"hh",
    "chunhe":"hh",
}
for value in set(user_1.values()):
    print(value)


