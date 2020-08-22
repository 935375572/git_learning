"""
处理多个列表
两个列表 一个列表包含店里供应的配料
另一个配料是客户点的配料
"""
requested_toppings = ["mushrooms", "extra", "extra cheese"]
user_toppings = ["mushrooms", "french fries", "extra cheese"]

for user_topping in user_toppings: # 循环客户点的配料
    if user_topping in requested_toppings: # 如果配料在requested_toppings 里
        print("adding" + user_topping)
    else:
        print("对不住，我们没有"+ user_topping)
print("您的披萨做好了")