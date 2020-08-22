"""
确定列表不是空
在制作披萨前检查顾客点的配料列表是否为空，如果列表是空的，就想顾客确认是否要点普通披萨，如果列表不为空
就像前面的示例那样制作披萨
"""
requested_toppings = []
if requested_toppings: # 至少包含一个元素时返回True 列表为空时返回false，由于此列表为空,是false，则直接输出else语句块的内容
    for requested_topping in requested_toppings:
        print("adding" + requested_topping)
    print("\nFinished making youe pizza!")
else:
    print("are you sure you want a plain pizza?")  # 你确定要点一份儿原味披萨吗
