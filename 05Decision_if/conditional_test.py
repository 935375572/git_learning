"""
条件测试
"""
car = "bmw"
print(car == "bmw")
print(car == "mazida")


names = ["zhangsan","lisi"]

if "zhangsan" in names:  # 张三在里面
    print("哈喽")

if "zhangsan" in names and "lisi" not in names:
    print("pr")


range1 = 20
range2 = 30
if range1<=20 and range2 <= 30:
    print("haore")

if range1<=20 or range2 <= 30:
    print("haore")