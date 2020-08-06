class Restaurant():
    def __init__(self, restaurant_name,cuisine_type):
     """
     python调用这个init方法创建Restaurant实例时，将自动传入实参self，他是一个指向实例本身的引用，让实例能访问类中的属性和方法
     以self为前缀的变量都可以供类中所有方法使用
     :param restaurant_name: 餐厅名称
     :param cuisine_type: 菜品样式
     :return:
     """
     # 初始化描述餐厅的属性
     self.restaurant_name = restaurant_name
     self.cuisine_type = cuisine_type

    def describe_reataurant(self):
        print("餐厅的名字是：" +self.restaurant_name)
        print("菜单的类型是：" + self.cuisine_type)

    def open_restaurant(self):
        print("菜单的类型是" +self.restaurant_name )

    def red(self):
        print("就餐人数是：" +str(self.number_of_people))
# 实例化
restaurant = Restaurant("123","asd")

# 访问属性
message = restaurant.restaurant_name
print(message)
message1 = restaurant.cuisine_type
print(message1)

# 调用方法
restaurant.describe_reataurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("234","xzx")
restaurant1.describe_reataurant()
restaurant2 = Restaurant("345","zxc")
restaurant2.describe_reataurant()
restaurant3 = Restaurant("456","asds")
restaurant3.describe_reataurant()
