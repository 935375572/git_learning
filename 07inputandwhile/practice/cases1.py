car = input("请问想要什么样的汽车呢： ")
print("我想要的汽车是：" + car)

message = input("请问有多少个用户用餐呢： ")
int_message = int(message)
if int_message > 8:
    print("不好意思，没有空卓了")
else:
    print("好的，收到")
