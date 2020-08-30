def make_shirt(chima, ziyang):
    print("尺码是：" + str(chima) + "\t" + "字样是： " + ziyang)

make_shirt(chima=23, ziyang="我爱你中国")



# 返回值return
def get_formatted_name(first_name, last_name):
    full_name = first_name + last_name
    return  full_name

# 需要提供一个变量 用来存储返回的值
public = get_formatted_name(first_name="张", last_name="三")
print(public)


# 让实参变成可选的   不是所有人都有中间名的  可选参数可以使用空字符串
def zhongjianming(first_name, last_name, zhongjianming=""):
    # 非空字符串解释为非true，如果调用了zhongjianming 则为true
    if zhongjianming:
        full_name = first_name + zhongjianming +last_name
    else:
        full_name = first_name +last_name
    return full_name
name = zhongjianming(first_name="张", last_name="三")
name1 = zhongjianming(first_name="张", zhongjianming="hesss", last_name="三")
print(name)
print(name1)

# 返回字典  接受姓名的组成部分，并返回一个表示人的字典
def persopn(first_name, last_name):
    persopns = {"first_name": first_name, "last_name": last_name }
    return  persopns

re = persopn("zhang", "sab")
for res, vale in re.items():
    print(res, vale)


def funames(first_name, last_name):
    funame = first_name +last_name
    return funame

# 无限循环
while True:
    print("你的姓名是什么")
    xing = input("你的姓是？")
    ming = input("你的名是？")

    jishou = funames(xing, ming)
    print(jishou)









