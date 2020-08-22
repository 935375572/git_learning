"""
嵌套
列表存储字典
场景：如果要管理N个外星人列表。 第一种方式是创建一个外星人列表。每个外星人是个字典，包含该外星人的各种信息
"""
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2] # 将所有的字典放到了列表中
for alien in aliens:
    print(alien)
print("\n")

"""
第二种 每个外星人自动生成
"""
alienss = []
for alien_number in range(31): # 返回一些数字，唯一的作用是告诉Python要重复这个循环30次
    new_alien = {"color": "green", "points": 5}  # 每次执行循环都创建个外星人
    alienss.append(new_alien) # 添加到aliens的末尾

for alien in alienss[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10

for alien in alienss[0:5]: # 使用切片打印前五个外星人
    print(alien)

print("一共创建了" + str(len(alienss)) + "个外星人")



