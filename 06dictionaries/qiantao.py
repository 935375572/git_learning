"""
嵌套
列表 存储字典
"""
# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个外星人
for alien_number in range(0,30):
    new_alien = {"颜色":"红色","分数":5}
    aliens.append(new_alien)

# 显示前五个颜色
for alien in aliens[:5]:
    print(alien)

for alien in aliens[0:3]:
    if alien["颜色"] == "红色":
        alien["颜色"] = "黄色"
        alien["分数"] = 5
for alien in aliens[0:5]:
    print(alien)
