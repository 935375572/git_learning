"""
五个最渴望去旅游的地方。 存储在一个列表欧中。
1 按照原始排列顺序打印该列表
2 使用sorted按照字母顺序打印，同时不要修改它
3 再次打印该列表 核实排列顺序未变
4 使用sorted按与字母顺序相反的顺序打印这个列表。同时不要修改它
5 再次打印该列表。核实排列顺序未变
6 使用reverse修改元素的排列顺序
7 使用sort修改该列表并打印
8 使用sort修改列表  并以相反的顺序打印
"""

difang = ["maerdaifu","daxidi","ruishi","shanghai","xian"]
print(difang)

print(sorted(difang)) # 临时排序
print(difang) # 再次打印该列表 顺序没有变

print(sorted(difang,reverse=True)) # 相反的顺序
print(difang) # 再次打印该列表 顺序没有变

difang.reverse()  # 相反排序 顺序确实变了
print(difang)
difang.reverse()
print(difang)

difang.sort() # 永久排序
print(difang)

difang.sort(reverse=True)
print(difang)


