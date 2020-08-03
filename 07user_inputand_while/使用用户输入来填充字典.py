# 创建一个调查程序，其中的循环每次执行时都提示输入 被调查者的名字和回答。 将手机的数据存储到一个字典中
responses = [] # 空字典

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    name = input("请问你叫什么名字")
    response = input("你喜欢动物吗")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("还有人吗(yes/no)")
    if repeat == "no":
        polling_active = False

# 调查结果，显示结果
print("\n------ poll results ------")
for name,response in responses.items():
    print(name + "would like to climb" + response + ".")