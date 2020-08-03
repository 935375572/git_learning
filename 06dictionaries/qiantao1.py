"""
字典存储列表  一个键存在多值的情况
"""
languages = {
    "jen":["python","Java"],
    "sarah":["C"],
    "zhangsan":["ruby","go"],
    "phil":["python","javascript"],
}

for name , language in languages.items():
    print(name)
    for language in language:
        print(language)

