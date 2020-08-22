users = ["admin", "zhangsan", "lisi", "wangwu", "zhaoliu"]
if users: #
    print("we need to find some users!") # 如果为空 输入 我们需要找到一些用户
for user in users:
    if user == "admin":
        print("hello "+user+",would you like to see a status report") # 你好，admin，你要看工作状况报告吗
    else:
        print("欢迎光临：" + user)


users = []
if users:
    print("we need to find some users!")  # 如果为空 输入 我们需要找到一些用户
    for user in users:
        if user == "admin":
            print("hello " + user + ",would you like to see a status report")  # 你好，admin，你要看工作状况报告吗
    else:
        print("欢迎光临：" + user)
print("helloworld\n")


current_users = ["admin", "zhangsan", "lisi", "wangwu", "zhaoliu"]
new_users = ["admin", "zhangsan", "maer", "tiantian", "xiaomeng"]

for new_user in new_users:
    if new_user in current_users:
        print(new_user + "已经被使用，请输入别的用户名")
    else:
        print(new_user + "还没有被使用,您可以使用")
