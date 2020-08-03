"""
int()函数将字符串变为数字
观察下列程序  判断一个人是否满足坐过山车的身高要求
"""
height = input("你的身高是多少")
height = int(height)
if height >= 36:
    print("满足要求了")
