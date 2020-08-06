### 函数  需要在程序中多次执行同一项任务的时候
# 定义函数
    def gree_user():
        print("hello world")

    gree_user()

# 向函数传递参数
    def gree_user(username):
        print("hello:" + username)

    # 调用函数 传递参数
    gree_user("jession")