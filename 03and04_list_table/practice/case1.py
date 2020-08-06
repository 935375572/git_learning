"""
3-1 将朋友的姓名存储在一个列表中，将其命名为names 依次访问列表的每个元素。从而将每个朋友的姓名都打印出来
3-2 不打印每个朋友的姓名，为每个人打印一条消息。每条消息都包含相同的问候语，但抬头为相应的朋友的姓名
3-3  创建一个多种通勤的方式的列表。根据列表打印一系列有关这些通勤方式的宣言
"""
names = ["张三","李四","王五"]
print(names[0])
print(names[1])
print(names[2])

message = names[0] + "你好，很高兴认识你"
message1 = names[1] + "你好，很高兴认识你"
message2 = names[2] + "你好，很高兴认识你\n"
print(message)
print(message1)
print(message2)

tongqins = ["摩托车","客车","轿车"]
message = "我喜欢的交通工具是"+tongqins[0]
message1 = "我喜欢的交通工具是"+tongqins[1]
message2 = "我喜欢的交通工具是"+tongqins[2]
print(message)
print(message1)
print(message2)