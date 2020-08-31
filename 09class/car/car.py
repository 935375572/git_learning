"""
表示汽车的类
"""
class Car():
    """模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print("汽车的里程是：" + str(self.odometer_reading))

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值
            拒绝将里程表往回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        # 将里程表读数增加指定的量
        self.odometer_reading += miles
