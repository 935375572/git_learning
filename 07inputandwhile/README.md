### while循环必须有停止运行的途径，避免无限循环。确认程序至少有一个地方能让循环体哦阿健为False或break语句得以执行
### 用户输入和while循环
    字符串转为数字使用int()函数
    hieght = input("告诉我你的年龄是多少?： ")
    ra_int = int(hieght)

    if ra_int >= 36:
        print("你的身高满足要求了")
    else:
        print("不好意思，你的身高还不够")
### 求模运算符 %
    如果一个数 可被另一个数整除  余数就为0，可以利用这一点判断一个数是奇数还是偶数
    ""
    判断奇数还是偶数
    """
    shuzi = input("给我一个数字，我能告诉你是奇数还是偶数： ")
    panduan = int(shuzi)
    if panduan % 2 == 0:
        print("这是个偶数呢")
    else:
        print("这是个奇数")
        
### while循环
    for循环针对集合中的每个元素的一个代码块儿
    而while循环不断的运行，知道指定的条件不满足为止
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
        
### 标志
    在要求很多条件都满足 才继续运行的程序中可以定义一个变量，用来判断整个程序是否处于
    活跃状态。这个变量就是标志，充当了程序的交通信号灯。
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
    
### 要立即退出while循环，不在运行循环中剩余的代码。也不管条件测试结果如何。可以用break语句。brake用于控制程序流程
    """
    让用户指出他到过哪些地方的程序。
    这个程序中，我们可以在用户输入"quit" 后使用break立即退出
    """
    message = "\n请输入您访问过的城市名称"
    message += "\n完成后输入quit"
    while True:
        city = input(message)
        if city == "quit":
            break
        else:
            print("我很想去的城市是：" + city)

### 返回循环开头，并根据条件测试结果决定是否继续执行循环，可以使用continue
    """
    continue 跳出当前循环到循环的开始
    """
    current = 1
    while current <= 10: # 小于等于10进入循环体
        current += 1 # 1+1 = 2
        if current % 2 == 0: # 如果2除以2=0 到开头开始
            continue
        else:
            print(current)

### for循环是遍历列表的有效方式，但在for循环中不应该修改列表，否则python难以跟踪其中的元素。要在遍历列表的同时对其
### 进行修改，可以使用while循环
    # 新注册但是还未验证的用户
    unconfirmed_users = ["alice", "brian", "candace"]
    # 已验证的用户列表
    confirmed_users = []

    while unconfirmed_users:
        new_user = unconfirmed_users.pop() # 把unconfirmed里的用户移除出来存放在 new_user 变量
        print("验证的用户是" + new_user)
        confirmed_users.append(new_user)

    # 显示已经验证的用户列表
    print("已经验证的是：")
    for confirmed_user in confirmed_users:
     print("\t"+ confirmed_user)
     
 