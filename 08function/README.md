### 需要在程序中多次执行同一项任务时，无需反复编写完成该任务的代码，而只需要调用函数即可
### def 关键字定义函数
### 位置实参：一定要保证实参的顺序和形参是一致的
    """
    简单函数定义
    """
    def greet_user():
        print("hello")
    greet_user()
    
    # greet_user("张三") 调用greet_user(username)，并在print函数中使用
    # username是形参   实参是调用函数时传递给函数的信息。。将实参“Jesse”传递给了函数gree_user("jesse")中
    def greet_user(username):
        print("hello"+ username)
    greet_user("张三")

### 位置实参，顺序一定不能错
    """
    位置实参
    """
    def animal_type(type, name):
        print("姓名是： " + name)
        print("类型是：" + type + ", 姓名是： " + name)
    
    animal_type("哺乳类", "狗狗")

### 位置实参
    """
    关键字实参 key-word形式
    """
    def animal_type(type, name):
        print("姓名是： " + name)
        print("类型是：" + type + ", 姓名是： " + name)
    
    animal_type(type="哺乳类", name="狗狗") 

### 默认值 如果有的形参有默认值 有的没有  没有的要放在前面
    """
    可以指定默认值。 不指定实参的时候 用的是默认值的值
    """
    def animal_type(type="爬虫", name="臭虫"):
        print("姓名是： " + name)
        print("类型是：" + type + ", 姓名是： " + name)
    
    animal_type()
    
### 返回值 return  使用return 将值返回到调用函数的代码行
    def get_foratted_name(firs_name, last_name):  # 通过参数接收姓名
        full_name = firs_name + last_name  # 将结果存储在full_name 中
        return full_name  # 返回调用函数行
    
    zhangsan = get_foratted_name(firs_name="张", last_name="三")
    print(zhangsan)

### 让实参变成可选的  使用默认值方式 传一个空值
# 让实参变成可选的
    def get_name(fist_name, last_name, zhongjianming=""):  # zhongjianming  中间名传一个空值  可选的
        if zhongjianming: # 非空代表true
            full_name = fist_name + zhongjianming + last_name
        else:
            full_name = fist_name + last_name
        return full_name
    
    
    print(get_name(fist_name="张", last_name="三"))
    print(get_name(fist_name="张", zhongjianming="小", last_name="三"))
    
### 返回字典
# 返回字典
    def build_person(fist_name, last_name):
        person = {"fist": fist_name, "last": last_name}
        return person
    
    
    print(build_person("jim", "sab"))
    
    
    def build_person(fist_name, last_name, age=""):
        person = {"fist": fist_name, "last": last_name}
        if age:
            person["age"] = age
        return person
    
    
    print(build_person("jim", "sab"))
    print(build_person("jim", "sab", 12))

### 组合使用while 和 函数
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

### 传递列表
# 传递列表
    def greet_user(names): # 接收一个名字列表 存到形参names中 names = username
        for name in names:
            msg = "你好啊：" + name
            print(msg)
    
    username = ["张三", "李四"]
    greet_user(username)
    
    
    # 3D打印公司 需要打印的设计存储在一个列表中   打印后移动到另一个列表中
    def print_models(unprinted_designs, completed_models):
        """
        模拟打印每个设计。直到没有未打印的设计为止
        打印每个设计后，都将其移动到列表  completed_models中
        :param unprinted_designs: 未印出的设计
        :param completed_models: 完成的设计
        :return:
        """
        while unprinted_designs:
            current = unprinted_designs.pop()
    
            # 模拟根据设计制作3D打印模型的过程
            print("打印模式" +current)
            completed_models.append(current)
    
    def show_completed_models(completed_models):
        """
        显示打印好的模型
        :param completed_models:
        :return:
        """
        for completed_model in completed_models:
            print(completed_model)
    
    # 创建列表
    unprinted_designs = ["iphone cases", "xiaomi"]
    completed_models = []
    
    print(unprinted_designs, completed_models)
    print_models(unprinted_designs[:], completed_models )   # 如果还想保留unprinted_designs 原始的数据  就使用[:] 副本   但尽量避免这样。 提高效率
    show_completed_models(completed_models)

### 传递任意数量的实参  *变量名
    # 传递任意数量的实参 *变量名   创建一个名为name的空元祖
    def name(*name):
        print(name)
    
    name("张三")
    name("张三", "李四")
    
# 使用任意数量的关键字实参  **变量名
# 传递任意数量的实参 *变量名   创建一个名为name的空元祖
    def name(*name):
        print(name)
    
    name("张三")
    name("张三", "李四")

# 使用任意数量的关键字实参  **变量名
    def user(fist_name, last_name, **user_info):
        person = {}
        person["姓"] = fist_name
        person["名"] = last_name
        for key , value in user_info.items():
            person[key] = value
        return person
    
    userss = user("张", "三", locaion = "sdfss")
    print(userss)




