def show_magicians(magicians):
    for magician in magicians:
        print(magician + ": 你好吗？")
magicians = ["zhangsan","lisi","wangwu"]


# 修改魔术师列表
def make_great(magicians):
    for magician in magicians:
        print(magician +"：修改了呢")
magicians = ["lisi", "wangwu", "wuha"]

show_magicians(magicians)
make_great(magicians)