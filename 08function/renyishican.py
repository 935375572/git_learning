# 传递任意数量的实参 *变量名   创建一个名为name的空元祖
def name(*name):
    print(name)

name("张三")
name("张三", "李四")

# 使用任意数量的关键字实参  **变量名
def user(fist_name, last_name, **user_info):
    person = {}
    person["姓"] = fist_name
    person["名"] = last_name
    for key , value in user_info.items():
        person[key] = value
    return person

userss = user("张", "三", locaion = "sdfss")
print(userss)
