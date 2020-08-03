"""
运动员队员列表  支持负数
"""

yundongyuans  = ["张三","李四","王五","赵六","三三"]
print(yundongyuans[0:3])  # 1-3 ['张三', '李四', '王五']
print(yundongyuans[1:4])  # 2-4 ['李四', '王五', '赵六']
print(yundongyuans[:3])   # 没指定 从头开始
print(yundongyuans[0:])   # 到结尾 ['张三', '李四', '王五', '赵六', '三三']


# 遍历切片
for yundongyuan in yundongyuans[:3]:
    print(yundongyuan)


# [:] 复制列表
yundongyuans  = ["张三","李四","王五","赵六","三三"]
huwu = yundongyuans[:]  # 将yundongyuans的内容给了huwu    不要huwu = yundongyuans  这是赋值不是将副本给huwu
print(yundongyuans)
print(huwu)