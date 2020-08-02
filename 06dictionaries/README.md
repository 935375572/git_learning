### 字典
    键值对 -- 用键访问关联的值
    字典 {键和值用冒号分隔，键值对之间用逗号分隔}
    增  删  改  查
### 遍历所有的键值对 items()方法
    for key,value in user_0.items():  # 声明两个变量来存储键和值
        print("\nkey:" + key)
        print("value:" +value)
### 遍历所有的键 keys()方法遍历所有的键 keys()方法   遍历字典时  会默认遍历所有的键。所以不用使用keys()方法也可以
    for key in user_0.keys():
        print("key:" + key)
### 遍历字典中所有的值 方法values()
    for value in user_0.values():
        print("value:" + value)
### 遍历值的时候 如果值出现重复，可以使用 集合 set 每个元素都是独一无二
    user_1 = {
        "user_name":"zhangsan",
        "first":"xiao",
        "last":"hh",
        "chunhe":"hh",
    }
    for value in set(user_1.values()):
        print(value)