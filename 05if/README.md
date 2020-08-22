###  条件测试
    == 检查是否相等
        a = b 表示把b赋值给a
        a == b 变量a的值是 b吗
    != 不等于
    
    检查多个条件都为true：条件测试1 and 条件测试2
    使用or，多个条件如果有一个条件为true就执行：  条件测试1 or 条件测试2 
    in : 检查特定值是否包含在列表中   
            yaoqing_persons = ["张三", "李四", "王五"]
                if "张三" in yaoqing_persons:
                    print("xxx")
    not in : 检查特定值不包含在列表中
                                          
    """
    有个汽车列表，将每个汽车的名字打印出来。汽车明"bmw"就全部大写显示出来  其他的首字母大写显示
    """
        cars = ["bmw", "kaisa", "mashang"]
        for car in cars:
            if car == "bmw":
                print(car.upper())
            else:
                print(car.title())
        
        # 观察不等于
        age = 19
        if age != 20:
            print("去一边去")
        
        # 观察 and
        if age >= 15 and age<=20:
            print("啦啦啦")
        
        # 观察or
        if age >= 15 or age<=21:
            print("哈哈哈")
        
        # 观察in包含
        cars = ["bmw", "kaisa", "mashang"]
        if "bmw" in cars:
            print("aaa")
### 布尔表达式   
    布尔表达式是条件测试的别名
    布尔表达式要么结果为True 要么就是false
    game_active = True
    can_edit = False
### if 语句
    如果要执行一个代码块，就是用if - elif -else
    如果要运行多个代码块，就是用一系列独立的if语句
    
    """
    简单的测试语句
    """
    age = 18
    if age >= 18:
        print("你已经到了投票的年龄了")
        # if 后缩进的代码  如果是True就都执行
        print("无哈")
    ·if else 非常适合要让Python执行两种操作之一的情形
        age = 17
        if age >= 18:
            print("你已经到了投票的年龄")
        else:
            print("你还没到投票的年龄")
    ·if-elif-else结构，检查超过两个的情形。可以有多个elif
        """
        4岁以下免费
        4-18岁收费5美元
        18岁(含)以上收费10
        """
        age = 12
        if age < 4:
            print("四岁以下免费")
        elif age < 18:
            print("收费5美元")
        else:
            print("收费10元")
    ·多个if条件。 上述仅适合用于只有一个条件满足的结尾，遇到了通过的测试，会跳过余下的测试
    ·在可能有多个条件为True，且需要在每个条件为True时都采取相应措施时，适合使用多个if
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
    
    """
    ·使用if语句处理列表
      如果青椒用完了，青椒用完了
    """
    requested_toppings = ["mushrooms" , "green peppers", "extra cheese"]
    for requested_topping in requested_toppings:
        if requested_topping == "green peppers": # 青椒已经没货了。如果点的是青椒，告诉用户没有了
            print("对不起青椒用完了")
        else:
            print("adding" + requested_topping)
    print("立刻送上来")
    
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