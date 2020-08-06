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