### 字典
    字典是一系列键-值对。 每个键和一个值相关联
    可以使用键访问与之相关的值
    字典用放在花括号中的
    alien_0 = {"color":"green","point":5}
    访问字典中的值： 字典名称[键]
    添加键值对：字典名[键] = 值
    删除键值对：del 字典名[键]
    修改字典中的值：字典名[键] = 新值
    遍历所有的键值对：
        for key, value in user_0.items():
    遍历所有的键：
        for key in user_0.keys():
    遍历所有的值：
        for value in user_0.values()
        值可能会有重复。如果想剔除重复项。可以使用set(user_0.values())   
    
    
    
    """
    访问字典中的值
    字典名[key]
    """
    aline_0 = {"color":"green","point":5}
    print(aline_0["color"])
    print(aline_0["point"])
    new_color = aline_0["color"]
    new_point = aline_0["point"]
    print("颜色是：" + new_color + "分数是：" + str(new_point))
    
    """
    添加键值对
    字典名[键] = 值
    """
    aline_0 = {"color":"green","point":5}
    # 增加字典中的值
    aline_0["地点"] = "上海"
    print(aline_0)   
    
    """
    删除键值对
    使用del关键字就永远消失了
    """
    alien_0 = {"color":"green", "points":5}
    del alien_0["color"]
    print(alien_0)
    
    """
    修改字典中的值
    """
    alien_0 = {"color":"green", "points":5}
    alien_0["color"] = "yellow"
    print(alien_0)
    
    """
    遍历字典
    遍历所有的键值对  items()
    """
    # 字典存储一名用户的用户名、名和姓
    user_0 = {
        "username": "efermi",
        "first": "enrico",
        "last": "fermi",
    }
    # 声明两个变量用来存储键和值 itmes()方法返回键值对存储到两个变量中
    for key, value in user_0.items():
        print(key + ": " + value)
        
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
    
    """
    字典存储列表
    当需要在字典中 将一个键关联到多个值时。可以在字典中嵌套一个列表
    披萨表皮和配料
    """
    pizza = {
        "crust": "thick",
        "toppings": ["mushrooms", "extra cheese"],
    }
    print("你点了一份" + pizza["crust"] + "的披萨") # you ordered a thick-crust pizza with the folowing toppings
    
    for topping in pizza["toppings"]:
        print(topping)
    
    favorite_languages = {
        "jen": ["python", "ruby"],
        "sarah": ["c"],
        "edward": ["ruby", "go"],
        "phil": ["python", "haskell"],
    }
    
    for name , languages in favorite_languages.items():
        print(name.title() + "s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
