### 函数input()获取用户输入
    message = input("告诉我你的年龄")  # 提示客户
    print(message) # 用户输入的信息存到message中并且打印出来
    如果提示内容过多可以使用 +=运算符
    message = "sdfsdfsdfsdxasdfsd"
    message += "sdfsdfszzz"
    name = input(message)
    print(name)
### 使用int()函数  将字符串变为数字
    """
    int()函数将字符串变为数字
    观察下列程序  判断一个人是否满足坐过山车的身高要求
    """
    height = input("你的身高是多少")
    height = int(height)
        if height >= 36:
        print("满足要求了")
### 使用标志
    pro = "要么输入一条消息 要么输入退出值 quit"
        biaozhi = True
        while biaozhi:
            message = input(pro)
            if message == "quit":
             biaozhi = False
            else:
                print(message)
### break 退出整个循环，不在执行余下的代码
    city = "你都去过哪些城市"
    # while True 将不断运行  直到遇到break
    while True:
        message = input(city)
        if message == "quit":
            break
        else:
            print(message)
### continue 返回到循环开头，并根据条件决定是否继续执行循环
    """
    如果被2整除 则不打印  结果是1  3  5  7  9
    """

    current_number = 0
    while current_number < 10:
       current_number+=1
        if current_number % 2 == 0:
         continue
        else:
            print(current_number)