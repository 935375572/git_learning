"""
让用户指出他到过哪些地方的程序。
这个程序中，我们可以在用户输入"quit" 后使用break立即退出
"""
message = "\n请输入您访问过的城市名称"
message += "\n完成后输入quit"
while True: # while True会不断的运行
    city = input(message)
    if city == "quit":
        break
    else:
        print("我很想去的城市是：" + city)
