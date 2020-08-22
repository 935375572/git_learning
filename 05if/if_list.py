"""
使用if语句处理列表
如果青椒用完了，青椒用完了
"""
requested_toppings = ["mushrooms" , "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers": # 青椒已经没货了。如果点的是青椒，告诉用户没有了
        print("对不起青椒用完了")
    else:
        print("adding" + requested_topping)
print("立刻送上来")