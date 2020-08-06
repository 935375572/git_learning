# 关键字实参

def describe_pet(name , type):
    print("动物名称：" + name)
    print("动物类型：" + type)

# 调用函数的时候 使用关键字实参的方式
describe_pet(name="狗狗" , type= "哺乳类")


# 可以给形参指定默认值.N个形参中如果有没有定义默认值的参数。 位置必须放在首位
def describe_pet(name = "123" , type="哺乳类动物"):
    print("动物名称：" + name)
    print("动物类型：" + type)

describe_pet()

"""
# 介绍尺码和字样 打印一个句子 说明尺码和字样
def make_shirt(chima,ziyang):
    print("尺码是：" +  chima + ",字样是：" + ziyang)
# 使用位置实参调用函数
make_shirt(str(2),"中国")
# 使用关键字实参调用函数
make_shirt(chima=str(2),ziyang="中国")
"""
# 默认情况下制作意见印有字样  “I love python”的大号T恤
def make_shirt(chima = "大号",ziyang = "I love python"):
    print("尺码是：" +  chima + ",字样是：" + ziyang)
make_shirt()
make_shirt(chima="中号")
make_shirt(chima="中号",ziyang="其他字样")

def describe_city(city_name,suoshu_guojia="中国"):
    print("说一下国家和城市吧\n")
    print("国家是：" + suoshu_guojia + " " + "城市是：" + city_name)
describe_city(city_name="长沙")
describe_city(city_name="赤峰")
describe_city(city_name="巴黎",suoshu_guojia="法国")


