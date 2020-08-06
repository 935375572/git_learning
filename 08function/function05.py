"""
让函数接收不同类型和数量的实参
"""
def make_pizza(*toppings):
    print(toppings)
make_pizza("猪肉")
make_pizza("猪肉",2,"sdfsdf")

# 使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """
    创建一个字典，其中包含我们知道的有关用户的一切
    **user_info  创建一个空字典
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key ,value in user_info.items():
        profile[key] = value
    return  profile

message = build_profile(first="123",last="asd",location="princeton",fieid="physics",abc="asf")
print(message)