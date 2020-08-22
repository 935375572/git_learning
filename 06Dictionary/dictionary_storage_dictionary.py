"""
字典存储字典
例如有多个网站，每个都有独特的用户名
可以在字典中将用户名作为建。降后将每位用户的信息存储在一个字典中。并将该字典作为与用户名相关联的值
"""

# 首先定义了字典，包含两个键
# 用户名aeinstrin 和 mcurie与每个键相关联的值都是一个字典
users = {
    "aeinstrin": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton"
    },

    "mcurie": {
        "first": "mare",
        "last": "curie",
        "location": "paris"
    },
}

for name, user_info in users.items():  # 将键存储在name中  值存储在user_info中
    print("用户名：" + name) # 将name打出来
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\t姓名是" + full_name)
    print("\t位置是" + location)