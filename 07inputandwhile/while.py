"""
while循环
"""
# 从数字1 到数字 5
current = 1
while current <= 5:
    print(current)
    current += 1

# 不断循环游戏程序，当用户输入 quit的时候结束程序
message = "有两个选择，要么输入一条消息"
message += "要么输入quit结束程序: "
user_message = ""
while user_message != "quit":
    user_message = input(message)
    print(user_message)


# 由于上述结果 连quit也会被打印出来。 优化一下

message = "有两个选择，要么输入一条消息"
message += "要么输入quit结束程序: "
user_message = ""
while user_message != "quit":
    user_message = input(message)
    if user_message != "quit":
        print(user_message)
