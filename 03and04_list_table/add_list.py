"""
增加列表元素
append(元素的值) : 在列表末尾添加元素
insert(索引,元素的值) ： 在列表中插入元素
"""
bicycless = ["trek","cannondale","redline","speciallized"]
bicycless.append("boy")
print(bicycless)

# 创建空列表非常常见，例如经常要等到程序运行后，才知道用户要在程序中存储哪些数据。可以首先创建一个空列表。用户存储用户
# 输入的值然后将新值加到列表中
bicycless = []
bicycless.append("boy")
bicycless.append("trek")
print(bicycless)

# 使用insert()方法 在列表中插入新元素
bicycless.insert(0,"haohan")
bicycless.insert(1,"hh")
print(bicycless)