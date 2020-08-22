# 包含各种三明治的名字
sandwich_orders = ["鸡肉三明治", "牛肉三明治", "猪肉三明治"]
# 完成了三明治
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("我给你做了" + sandwich)
    finished = finished_sandwiches.append(sandwich)

for finished_sandwiche in finished_sandwiches:
    print("已经完成了"+ finished_sandwiche)


sandwich_orders = ["鸡肉三明治", "牛肉三明治", "猪肉三明治", "五香烟熏牛肉", "五香烟熏牛肉", "五香烟熏牛肉", "五香烟熏牛肉"]
print("五香烟熏牛肉已经卖完了")

while "五香烟熏牛肉" in sandwich_orders:
        sandwich_orders.remove("五香烟熏牛肉")
for sandwich_order in sandwich_orders:
    print("现在只剩下" + sandwich_order + "了")

dujia = {}
active = True
while active:
    name = input("请问你叫什么名字呢？")
    didian = input("告诉我你喜欢的旅游地方是哪里呢？")

    dujia[name] = didian

    user = input("还有其他的地方吗？yes/no")
    if user == "no":
        active = False

for name, value in dujia.items():
    print(name + "喜欢的地方是" + value)

