# 创建Dog类
class Dog():  # 首字母大写
    def __init__(self, name, age):  # 让实例能够访问类中的属性和方法
        self.name = name  # 以self为前缀的变量都可供类中的所有方法使用
        self.age = age

    def sit(self):
        print(self.name + "is now sitting")

    def roll_over(self):
        print(self.name +"roll_over")

# 根据类创建实例
my_dog = Dog("小小", 3)  #调用Dog类中_init_方法
print("我狗的名字是" + my_dog.name)
print("我狗的年龄是" + str(my_dog.age))
my_dog.sit()  # 调用方法
my_dog.roll_over()

