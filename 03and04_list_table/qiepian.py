number = ["a", "b", "c", "d", "e"]
print(number[0:3]) # ['a', 'b', 'c']
print(number[2:4]) # 结果是  c  d

number = ["a", "b", "c", "d", "e"]
# 将number的副本内容复制到my_number里，不可以my_number = number  这复制的就不是副本了
my_number = number[:]
print(my_number)
# 为了证实确实有两个列表，增加不同的内容
number.append("tiantian")
my_number.append("哈哈哈")
print(number)
print(my_number)