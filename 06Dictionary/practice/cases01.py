favorite_languages = {
    "jen":"python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

firends = ["phil","jen"]
# 循环favorite_languages中的所有键
for name in favorite_languages.keys():
    print(name) # 打印里面的名字
    if name in firends: # 如果名字在firends里
        print(name + "喜欢的语言是" + favorite_languages[name]) # 通过建访问值
