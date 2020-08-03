alien_color = "yellow"

"""
# 如果是绿色 则通过
if alien_color == "green":
    print("获得了五个点")

# 如果不是绿色  没有输出
if alien_color != "green":
    print()
"""
if alien_color == "green":
    print("获得了五个点")
if alien_color != "green":
    print("获得了10个点\n")

if alien_color == "green":
    print("获得了五个点")
else:
    print("获得了10个点\n")

# 定义一个空列表
pissas = []
# python将在列表至少有一个内容时为true  没有内容时为false
# 先判断下是否为空  如果pissas里有内容，则执行循环
if pissas:
    for pissa in pissas:
        print("想吃什么披萨")
else:
    print("对不起，现在什么都没有了\n")


# 两个列表使用
pissas = ["猪肉","牛肉","鱼肉"]  # pissas列表
user_pissas = ["猪肉","牛肉","养肉"] # 客户点的菜

for user_pissa in user_pissas:
    if user_pissa in pissas:
        print("你点的我们这都有")
    else:
        print("不要意思没有羊肉\n")

user_names = ["admin","xiaozhang","xiaoli","zhangsan","liyuchun"]
if user_names:
    for user_name in user_names:
        if "admin" in user_name:
            print("你好啊admin")
    else :
        print("hello")

