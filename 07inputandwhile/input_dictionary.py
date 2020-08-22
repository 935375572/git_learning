responses = {}
polling_active = True
while polling_active:
    name = input("请问你的名字是： ")
    message = input("你喜欢爬哪座山： ")

    responses[name] = message

    repeat = input("你还有喜欢的山吗，yes/no: ")
    if repeat == "no":
        polling_active = False

print("调查结果：")
for name , value in responses.items():
    print(name + "喜欢爬的山是" + value)
