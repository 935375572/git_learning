"""
# 组合使用while循环  给用户打招呼
def get_formatted_nam(first_name, last_name):
    full_name = first_name +last_name
    return full_name

while True: # 这是一个无限循环
    print("告诉我你的姓名可以吗？")
    xing = input("姓是什么？")
    ming = input("名是什么？")

    formatted = get_formatted_nam(first_name="张", last_name="三")
    print("你好啊" + formatted)
"""
# 优化上面的代码。 让其有退出条件
def get_formatted_nam(first_name, last_name):
    full_name = first_name + last_name
    return full_name

while True: # 这是一个无限循环
    print("告诉我你的姓名可以吗？")

    xing = input("姓是什么？")
    if xing == "quti":
        break

    ming = input("名是什么？")
    if ming == "quti":
        break

    formatted = get_formatted_nam(first_name=xing, last_name=ming)
    print("你好啊" + formatted)