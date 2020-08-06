# 创建一个列表。邀请至少三人共进晚餐，然后使用这个表打印消息。邀请这些人来共进晚餐
yaoqing_persons = ["张三", "李四", "王五"]
print(yaoqing_persons[0] + "你好，与我共进晚餐吧")
print(yaoqing_persons[1] + "你好，与我共进晚餐吧")
print(yaoqing_persons[2] + "你好，与我共进晚餐吧")
print(yaoqing_persons[0] + "不能来赴约了\n")

# 张三不能来了。名单要换成赵六，再次对每个人发出邀请
yaoqing_persons[0] = "赵六"
print(yaoqing_persons[0] + "你好，与我共进晚餐吧")
print(yaoqing_persons[1] + "你好，与我共进晚餐吧")
print(yaoqing_persons[2] + "你好，与我共进晚餐吧")
print("餐桌大了，可以在邀请三个人\n")

# 找到了更大的餐桌。在邀请三个人
yaoqing_persons.insert(0,"刘天儿")
yaoqing_persons.insert(2,"郭得友")
yaoqing_persons.append("顾影")
print(yaoqing_persons[0] + "你好，与我共进晚餐吧")
print(yaoqing_persons[1] + "你好，与我共进晚餐吧")
print(yaoqing_persons[2] + "你好，与我共进晚餐吧")
print(yaoqing_persons[3] + "你好，与我共进晚餐吧")
print(yaoqing_persons[4] + "你好，与我共进晚餐吧")
print(yaoqing_persons[5] + "你好，与我共进晚餐吧")
print("不好意思各位，新买的餐桌只能邀请两位\n")

liutian = yaoqing_persons.pop()
print(liutian + ", 实在不好意思了")
zhaoliu = yaoqing_persons.pop()
print(zhaoliu + ", 实在不好意思了")
guodeyou = yaoqing_persons.pop()
print(guodeyou + ", 实在不好意思了")
lisi = yaoqing_persons.pop()
print(lisi + ", 实在不好意思了")

print(yaoqing_persons[0] + ", 你依然在名单里")
print(yaoqing_persons[1] + ", 你依然在名单里")

del yaoqing_persons[0]
del yaoqing_persons[0]
print(yaoqing_persons)



