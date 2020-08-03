"""
方法 sort() 对列表进行永久排序
"""
names = ["zhangsan","lisi","wangwu"]
names.sort()
print(names)

# sort(reverse = True) 进行相反排序
names.sort(reverse=True)
print(names)

# soeted进行临时排序
print(sorted(names))
print(names)  # 再调用一次即可恢复
# soeted 也可以使用reverse
print(sorted(names,reverse=True))

# 使用reverse 相反顺序排序
print(names)
names.reverse()
print(names)

# 使用len方法统计个数
print(len(names))


