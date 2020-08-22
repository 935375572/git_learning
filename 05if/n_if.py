"""
多个if条件
如果顾客点了两种配料，就需要确保在比萨中包含这些配料
不管前一个if语句是否通过都会执行下一个if条件。 每个都是单独的。 不想if else 如果一个通过余下的不执行
"""
requested_toppings = ["mushrooms", "extra", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("adding mushrooms")
if "pepperoni" in requested_toppings:
    print("adding pepperoni")
if "extra cheese" in requested_toppings:
    print("adding extra cheese")
print("\nFinished making your pizza!")  # 你的披萨做好了