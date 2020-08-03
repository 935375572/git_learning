pro = "要么输入一条消息 要么输入退出值 quit"
message = ""
while message != "quit":
    message = input(pro)
    # bprint(message)

    # 优化此程序  以上程序唯一不足的是 如果输入quit  那么quit也会打印出来
    if message != "quit":
        print(message)

# 使用标志
pro = "要么输入一条消息 要么输入退出值 quit"
biaozhi = True
while biaozhi:
    message = input(pro)
    if message == "quit":
        biaozhi = False
    else:
        print(message)

