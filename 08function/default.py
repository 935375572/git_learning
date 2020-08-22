"""
可以指定默认值。 不指定实参的时候 用的是默认值的值
"""
def animal_type(type="爬虫",name="臭虫" ):
    print("姓名是： " + name)
    print("类型是：" + type + ", 姓名是： " + name)

animal_type()