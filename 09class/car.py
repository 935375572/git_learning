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

    def update_odometer(self, mileage):
        self.odometer_readint = mileage

my_car = Car("audi", "a4", 2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()


# 修改属性的值
# 1 直接修改属性的值
my_car.odometer_readint = 20
my_car.read_odometer()
# 2通过方法修改属性的值
#     def read_odometer(self):
#         print("这辆车有" + str(self.odometer_readint) + "里程数")
my_car.update_odometer(23)
my_car.read_odometer()

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