"""
嵌套
列表 存储字典
字典 存储列表
字典 存储字典
"""
# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个外星人
for alien_number in range(30):
    new_alien = {"颜色","红色","分数",5}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)

# 显示一共创建了多少外星人
print("一共创建了：" + str(len(aliens)) + "个外星人")