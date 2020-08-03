"""
字典存储字典
两个用户aeinstein 和 mcurie    姓名和居住地
"""
users = {
    "aeinstein":{"first":"albert","last":"einstein","location":"princeton"},
    "mcurie":{"first":"marie","last":"curie","location":"paris"}
}

for key , value in users.items():
    print(key)
    full_name = value["first"] + " " + value["last"]
    location = value["location"]
    print(full_name)
    print(location)
