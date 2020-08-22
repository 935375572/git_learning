"""
使用标志
"""
message = "有两个选择，要么输入一条消息"
message += "要么输入quit结束程序: "
active = True
# 增加了个标志，只要变量active是true，程序就继续运行
while active:
    pro = input(message)
    if pro == "quit":
        active = False
    else:
        print(pro)

