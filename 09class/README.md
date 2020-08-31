### 类
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

### 属性必须有默认值
    class Car():
        def __init__(self, make, model, year):
            """
            :param make:  制作
            :param model: 模型
            :param year:  年份
            :odometer_readint: 里程表
            """
            self.make = make
            self.model = model
            self.year = year
            self.odometer_readint = 0 # 增加里程表  默认值是0
        def get_descriptive_name(self):
            long_name = str(self.year) + " " + self.make + " " + self.model
            return  long_name
    
        def read_odometer(self):
            print("这辆车有" + str(self.odometer_readint) + "里程数")
    my_car = Car("audi", "a4", 2016)
    print(my_car.get_descriptive_name())
    my_car.read_odometer()
    
### 给属性指定默认值和修改属性的值
    # 修改属性的值
    # 1 直接修改属性的值
    my_car.odometer_readint = 20
    my_car.read_odometer()
    # 2通过方法修改属性的值
    #     def read_odometer(self):
    #         print("这辆车有" + str(self.odometer_readint) + "里程数")
    my_car.update_odometer(23)
    my_car.read_odometer()

### 继承
      class ElectricCar(Car):
        def __init__(self, make, model, year):
            # 初始化父类的属性
            super().__init__(make, model, year)
    
    my_tesla = ElectricCar("asds", "model", 2020)
    print(my_tesla.get_descriptive_name())

### 给子类定义属性 和 方法
    class ElectricCar(Car):
        def __init__(self, make, model, year):
            # 初始化父类的属性
            super().__init__(make, model, year)
            self.battery_size = 70
    
        def describe_battery(self):
            print("这辆车有一个"+ str(self.battery_size) + "千瓦时的电池")
    my_tesla = ElectricCar("asds", "model", 2020)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    
### from 模块名 import 类名
### from 模块名 import 类名1 ， 类名2
### import 模块名   导入整个模块
    调用的时候 模块名。类名（实参。。。）
