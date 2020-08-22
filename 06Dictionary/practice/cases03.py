river = {
    "尼罗河": "中国",
    "赛鼎湖": "中华人民共和国",
    "贝加尔湖": "中华",
}

for heliu ,guojia in river.items():
    print(heliu + "经过" + guojia)
print("\n")

for heliu in river.keys():
    print("显示每个河流的名字" + heliu)
print("\n")

for guojia in river.values():
    print("显示每个国家的名字" + guojia)
print("\n")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
names = ["jen", "sarah"]

for favorite_language in favorite_languages.keys():
    if favorite_language in names:
        print(favorite_language + "感谢你啊")
    elif favorite_language not in names:
        print(favorite_language + "欢迎来参加调研啊")


