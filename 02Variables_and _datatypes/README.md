### 第二章 变量和简单的数据类型
    变量名只能包含字母、数字、下划线(不能是数字开头)
    变量名不能使用空格，可以用下划线分隔单词
    不能使用关键字，见名知意
    少用小写字母i和大写的O  特别像1和0
    变量名使用小写，这不是规定，是规范
    删除空白：
        删除末尾空白：rstrip()
        删除开头空白：lstrip()
        删除两端空白：strip()
    字符串大小写处理     
        upper()  字符串转大写
        lower()  字符串转小写
        title()  字符串首字母大写
        
    # 将 "Hello Python world" 存储在变量 message中
    message = "Hello Python world"
    # 打印message关联的值
    print(message)
    
    """
    数据类型：字符串
    用引号括起的都是字符串：单引号和双引号都可以
    """
    # 使用方法修改字符串的大小写
    string = "ada name"
    # 使用title()方法将字符串首字母大写显示并输出:对string变量执行title方法
    print(string.title())
    # 使用title()方法将字符串全部内容大写显示并输出:对string变量执行upper方法
    print(string.upper())
    # 使用title()方法将字符串全部内容小写显示并输出:对string变量执行lower方法
    print(string.lower())
    
    """
    字符串连接  使用+号
    """
    # 将姓和名 存储在不同的变量中，显示姓名时合二为一
    first_name = "san"  # 名
    last_name = "zhang"   # 姓
    # 名 + 姓 得到完整的名字 并输出
    full_name = first_name + " " + last_name
    print(full_name)
    
    """
    制表符  \t
    换行符  \n
    """
    message = "\thello\tbo"
    print(message)

    message = "\nhellp\nbo"
    print(message)

    message = "languages:\n\tjava\n\tpython\n\tC++"
    print(message)
    
    """
    删除空白  删除末尾空白：rstrip()
              删除开头空白：lstrip()
              删除两端空白：strip()
    """
    message = "hello "
    # 输出hello
    print(message)
    # 对message的内容做删除末尾空白处理
    print(message.rstrip())
    # 再次执行 恢复到原来的样子
    print(message)
    # 删除末尾的空白，再将新值存储到原来的变量中。
    message = message.rstrip()
    # 在输出就依然是处理后的数据
    print(message)
    
    # 前面有空白 使用lstrip()删除
    name = " zhangsan"
    print(name)
    name = name.lstrip()
    print(name)
    
    # 两边有空白 使用strip()删除
    name = " zhangsan "
    print(name)
    name = name.strip()
    print(name)