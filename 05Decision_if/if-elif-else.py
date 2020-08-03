"""
4岁以下免费
4-18岁收费5美元
18岁(含)以上10美元
"""

age =14
if age < 4 :
    print("免费喔")
elif age >=4 and age<18:
    print("收费五美元")
else:
    print("10美元")


# 可以使用多个elif
age =14
if age < 4 :
    print("免费喔")
elif age >=4 and age<18:
    print("收费五美元")
elif age >=18 and age<=60:
    print("20")
else:
    print("10美元")
