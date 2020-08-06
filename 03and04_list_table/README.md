### 列表
    元组：不可修改的使用圆括号()来表示，用逗号分隔其中的元素
    列表是有序集合
    列表包括多个元素，给列表指定一个表示复数的名称如：names
    列表使用方括号[]来表示，用逗号分隔其中的元素
    索引是0不是一  
    增加列表元素：
        append(元素的值) : 在列表末尾添加元素
        insert(索引,元素的值) ： 在列表中插入元素
    删除元素：
        知道索引位置并且想永久删除 使用del关键字
            del 列表名称[索引]
        pop()方法，删除末尾元素。删除之后可以将元素存储一个变量中，后续可以继续使用(只在列表删除而已)
            列表名称.pop()
        pop(索引)方法，删除任意位置的元素
            列表名称.pop(索引)
        根据值删除元素使用remove(元素值)，删除之后也可以接着使用他的值。如果值重复可以使用for循环加判断
            列表名称.remove(元素值内容)
    修改列表的元素：
        列表变量名[索引] = 新值
    访问列表元素（查询）  ： 
        列表变量名[索引]   索引可以为负数 -1是最后一个元素
    列表排序：
        使用sort()方法对列表进行永久性的排序
        使用sort(reverse=True) 相反顺序永久排序
        使用sorted() 进行临时性排序，原始顺序不变，也可以使用reverse=True
        使用reverse()翻转列表元素的顺序  永久性的，但可随时恢复，再调用一次reverse即可
    len()计算列表长度   
    range()函数  生成一系列数字
    list()函数 可以让range()生成的数字形成数字列表
        number = list(range(1,30)) # 生成1-29个数字 并使用list函数转换成列表
    对数字列表执行简单的统计计算
        sum(列表名)  求和  
        max(列表名)  最大值
        min(列表名)  最小值    
    切片(使用列表的一部分)：结束索引+1,支持负数
        列表名[第一个索引 :第二个索引+1]
        列表名[:第二个索引]  从头开始
        列表名[第一个索引:结尾]
        列表名[:] 复制列表内容
        
        
        
    
    
    
    访问列表
        """
        自行车品牌
        """
        bicycless = ["trek","cannondale","redline","speciallized"]
        # 输出列表。 包括方括号。但这不是客户想要的
        print(bicycless)
    
        """
        访问列表(查询)
        """
        bicycless = ["trek","cannondale","redline","speciallized"]
        # 输出第一个元素内容，索引为0。 方括号不会显示出来
        print(bicycless[0])
        print(bicycless[0].title())
        # 允许为负数 -1最后一个元素 。以此类推
        print(bicycless[-1])
        
    增加列表元素
        append(元素的值) : 在列表末尾添加元素
        insert(索引,元素的值) ： 在列表中插入元素
        
        bicycless = ["trek","cannondale","redline","speciallized"]
        bicycless.append("boy")
        print(bicycless)

        # 创建空列表非常常见，例如经常要等到程序运行后，才知道用户要在程序中存储哪些数据。可以首先创建一个空列表。用户存储用户
        # 输入的值然后将新值加到列表中
        bicycless = []
        bicycless.append("boy")
        bicycless.append("trek")
        print(bicycless)
        
        # 使用insert()方法 在列表中插入新元素
        bicycless.insert(0,"haohan")
        bicycless.insert(1,"hh")
        print(bicycless)
    修改列表元素：
        bicycless = ["trek","cannondale","redline","speciallized"]
        bicycless[0] = "baby"
        print(bicycless)
    删除列表元素
        bicycless = ["trek","cannondale","redline","speciallized"]
        
        # 使用remove根据值删除
        bicycless.remove("trek")
        print(bicycless)
        
        # 使用del关键字永久删除
        del bicycless[0]
        print(bicycless)
        
        # 使用pop()删除末尾并继续使用他的值
        bicycless.pop()
        print(bicycless)
        new_zhi= bicycless.pop()
        print(new_zhi + "非常棒啊")
        print(bicycless)
        
    列表排序：    
        # 使用sort()方法对列表进行永久性的排序
        # 汽车列表，要让汽车的字母顺序排列
        cars = ["bmw", "audi", "toyota", "subaru"]
        cars.sort()
        print(cars)  # 输出结果 ['audi', 'bmw', 'subaru', 'toyota']

        # 永久性的按照字母顺序相反的
        cars.sort(reverse=True)
        print(cars)

        # 观察sorted()进行临时性排序
        cars = ["bmw", "audi", "toyota", "subaru"]
        print(cars) # 原始顺序
        print(sorted(cars)) # 临时排好的顺序
        print(cars) # 原来的顺序
        
        # 观察reverse()进行排序
        cars = ["bmw", "audi", "toyota", "subaru"]
        cars.reverse()
        print(cars)
        cars.reverse()
        print(cars)
    
    计算列表长度：
        cars = ["bmw", "audi", "toyota", "subaru"]
        print(len(cars)) # 计算列表长度
    
    # 生成1-29个数字  并使用list函数将数字生成列表
        message = list(range(1,30))
        print(message)
        # 可以指定步长 从1开始数 1+2=3 3+2 =5...   结果是1 3 5 7 9 11
        message = list(range(1,12,2)) 
        print(message)
    
    切片
        number = ["a", "b", "c", "d", "e"]
        print(number[0:3]) # ['a', 'b', 'c']
        print(number[2:4]) # 结果是  c  d
        
        # [:]复制副本
        number = ["a", "b", "c", "d", "e"]
        # 将number的副本内容复制到my_number里，不可以my_number = number  这复制的就不是副本了
        my_number = number[:]  # 将number的副本内容复制到my_number里
        print(my_number)
        # 为了证实确实有两个列表，增加不同的内容
        number.append("tiantian")
        my_number.append("哈哈哈")
        print(number)
        print(my_number)