"""
退出整个循环
"""
pro = "你都去过哪些城市"
# while True 将不断运行  直到遇到break
while True:
    message = input(pro)
    if message == "quit":
        break
    else:
        print(message)