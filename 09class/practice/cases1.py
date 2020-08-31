class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """
        param restaurant_name:  餐厅的名字
        :param cuisine_type: 菜式
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # 餐厅的描述
    def describe_restaurant(self):
        print("餐厅的名字是：" + self.restaurant_name + " " + "菜式是：" + self.cuisine_type )

    def open_restaurant(self):
        print(self.restaurant_name + "现在正在营业")

restaurant = Restaurant("井格", "火锅")
restaurant.describe_restaurant()
restaurant.open_restaurant()
