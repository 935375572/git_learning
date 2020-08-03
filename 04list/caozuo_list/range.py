"""
range(开始,结束差一行,步长) 生成一系列数字
list()函数可以将range()生成的函数称为列表
sum()  求和
max() 最大
min() 最小
"""
for rangee in range(1,6): # 遍历1-5个数
    print(rangee)

numbers = list(range(1,5))
print(numbers)

# 指定步长  打印1-10内的偶数
numbers = list(range(2,11,2)) # 从2开始数  不断加2 直到达到或超过最终值
print(numbers)

# 对数字列表简单的统计计算
numbers = [-1,2,3,32,123,565,777]
print(sum(numbers))
print(max(numbers))
print(min(numbers))