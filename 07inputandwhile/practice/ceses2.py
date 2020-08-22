pro = "请你输一下披萨配料: "
while True: # 一直循环
    message = input(pro)
    if message == "quit": # 如果消息是quit 此循环结束
        break
    else:
        print(message)
