"""
假设有个列表   包含注册但为未验证的网站用户   验证这些用户后，移动到注册列表里
"""
unconfirmed_users = ["zhangsan","lisi","wangwu"] # 未验证
confirmed_users = [] # 注册
while unconfirmed_users:
    unconfirmed_user = unconfirmed_users.pop()
    confirmed_users.append(unconfirmed_user)


for confirmed_user in confirmed_users:
    print(confirmed_user)

# 根据值来删除元素 remove方法，使用while循环来解决重复值得问题
names = ["zhangsan","lisi","wangwu","zhangsan"]
print(names)

while names:
    if "zhangsan" in names:
        names.remove("zhangsan")
        print(names)

