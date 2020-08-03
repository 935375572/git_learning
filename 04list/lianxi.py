"""
创建一个列表。包含至少三个想要邀请的人，然后，使用这个列表打印消息。邀请这些人与你共进晚餐
"""
names = ["张三","李四","王五"]

# 向每位发出邀请
message = "欢迎光临："+ names[0] + "来参加我的晚宴，我很荣幸"
message1 = "欢迎光临："+ names[1] + "来参加我的晚宴，我很荣幸"
message2 = "欢迎光临："+ names[2] + "来参加我的晚宴，我很荣幸"
message3 = "很遗憾" + names[0] + "同学不能来我的晚宴了，我需要在邀请一位\n"
print(message)
print(message1)
print(message2)
print(message3)
# 一共有多少位来参加
print("一共有" + str(len(names)) + "位来参加聚会")

# 修改嘉宾名单。张三替换为刘二
names[0] = "刘二"
message = "欢迎光临："+ names[0] + "来参加我的晚宴，我很荣幸"
message1 = "欢迎光临："+ names[1] + "来参加我的晚宴，我很荣幸"
message2 = "欢迎光临："+ names[2] + "来参加我的晚宴，我很荣幸"
message3 = "各位，我现在有个更大的餐桌啦\n"
print(message)
print(message1)
print(message2)
print(message3)

# 新嘉宾放在名单最前面
names.insert(0,"赵四")
# 王静在最中间
names.insert(2,"王静")
# 使用append方法放在最后面
names.append("三三")
print(names)
message0 = "欢迎光临："+ names[0] + "来参加我的晚宴，我很荣幸"
message1 = "欢迎光临："+ names[1] + "来参加我的晚宴，我很荣幸"
message2 = "欢迎光临："+ names[2] + "来参加我的晚宴，我很荣幸"
message3 = "欢迎光临："+ names[3] + "来参加我的晚宴，我很荣幸"
message4 = "欢迎光临："+ names[4] + "来参加我的晚宴，我很荣幸"
message5 = "欢迎光临："+ names[5] + "来参加我的晚宴，我很荣幸"
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print("不好意思各位，我现在只能邀请两位人员了\n")

# 缩减名单  现在只能邀请两位嘉宾了
# 使用pop不断的删除名单中的嘉宾。直到有两位嘉宾为止。每次弹出一位时，都打印一条消息。我很抱歉。无法邀请你来共进晚餐
zhaosi = names.pop(0)
print(zhaosi + "，我很抱歉，无法邀请你来共进晚餐")
liuer = names.pop(0)
print(liuer + "，我很抱歉，无法邀请你来共进晚餐")
wangjing = names.pop(0)
print(wangjing + "，我很抱歉，无法邀请你来共进晚餐")
lisi = names.pop(0)
print(lisi + "，我很抱歉，无法邀请你来共进晚餐\n")
print(names)

# 剩下的王五和三三依旧可以接受邀请
print(names[0] + "，你还在名单中哟，别忘记来参加")
print(names[1] + "，你还在名单中哟，别忘记来参加\n")
# 一共有多少位来参加
print("一共有" + str(len(names)) + "位来参加聚会")

# 删除所有名单
del names[0]
del names[0]

# 一共有多少位来参加
print("一共有" + str(len(names)) + "位来参加聚会")
print(names)
