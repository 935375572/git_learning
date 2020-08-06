"""
删除
"""
bicycless = ["trek","cannondale","redline","speciallized"]

# 使用remove根据值删除
bicycless.remove("trek")
print(bicycless)

# 使用del关键字永久删除
del bicycless[0]
print(bicycless)

# 使用pop()删除末尾并继续使用他的值
bicycless.pop()
print(bicycless)
new_zhi= bicycless.pop()
print(new_zhi + "非常棒啊")
print(bicycless)