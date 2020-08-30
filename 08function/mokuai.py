# 模块
def make_pizza(size, *toppings):
    print("尺寸是："  + str(size) + "用以下配料将披萨英寸")
    for topping in toppings:
        print(topping)
