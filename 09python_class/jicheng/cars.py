class Car():
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        "返回描述性信息"
        long_name = str(self.year) + " " + self.make + " " + self.model
        return  long_name

my_new_car = Car(make="12",model="`12",year=12)
print(my_new_car.get_descriptive_name())

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        初始化父类的属性
        :param make:
        :param model:
        :param year:
        """
        # 初始化父类的属性  super()函数帮助子类和父类关联起来
        # 在初始化电动汽车的属性
        super().__init__(make, model, year)
        self.dianping = 70

    # 子类自己的方法
    def zileifangfa(self):
        print("我的电瓶容量是：" + str(self.dianping))

    def get_descriptive_name(self):
        print("重写父类的方法")

my_electricCar = ElectricCar(make="13",model="`11",year=16)
print(my_electricCar.get_descriptive_name())
my_electricCar.zileifangfa()