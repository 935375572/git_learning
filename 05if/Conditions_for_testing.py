"""
有个汽车列表，将每个汽车的名字打印出来。汽车明"bmw"就全部大写显示出来  其他的首字母大写显示
"""
cars = ["bmw", "kaisa", "mashang"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# 观察不等于
age = 19
if age != 20:
    print("去一边去")

# 观察 and
if age >= 15 and age<=20:
    print("啦啦啦")

# 观察or
if age >= 15 or age<=21:
    print("哈哈哈")

# 观察in包含
cars = ["bmw", "kaisa", "mashang"]
if "bmw" in cars:
    print("aaa")