"""
遍历字典
遍历所有的键值对  items()
"""
# 字典存储一名用户的用户名、名和姓
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
    "uee": "fermi",
}
# 声明两个变量用来存储键和值 itmes()方法返回键值对存储到两个变量中
for key, value in user_0.items():
    print(key + ": " + value)

"""
遍历字典 
遍历所有的键  keys()
默认就是遍历所有的键  也可以不指定keys()
"""
for key in user_0.keys():
    print(key)

"""
遍历字典 
遍历所有的值  values()
"""
for value in user_0.values():
    print("值是：" + value)

"""
剔除重复值
"""
for value in set(user_0.values()):
    print("剔除重复值之后是：" + value)





