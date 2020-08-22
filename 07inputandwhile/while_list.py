# 新注册但是还未验证的用户
unconfirmed_users = ["alice", "brian", "candace"]
# 已验证的用户列表
confirmed_users = []

while unconfirmed_users:
    new_user = unconfirmed_users.pop() # 把unconfirmed里的用户移除出来存放在 new_user 变量
    print("验证的用户是" + new_user)
    confirmed_users.append(new_user)

# 显示已经验证的用户列表
print("已经验证的是：")
for confirmed_user in confirmed_users:
    print("\t"+ confirmed_user)