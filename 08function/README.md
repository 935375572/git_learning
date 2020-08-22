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
    
### 返回值 return


