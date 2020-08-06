# 使用sort()方法对列表进行永久性的排序
# 汽车列表，要让汽车的字母顺序排列
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)  # 输出结果 ['audi', 'bmw', 'subaru', 'toyota']

# 永久性的按照字母顺序相反的
cars.sort(reverse=True)
print(cars)

# 观察sorted()进行临时性排序
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) # 原始顺序
print(sorted(cars)) # 临时排好的顺序
print(cars) # 原来的顺序

# 观察reverse()进行排序
cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)
cars.reverse()
print(cars)



