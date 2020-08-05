"""
2-3 将用户的姓名存储到一个变量中，并向该用户显示一条消息。显示一句话1
2-4 调整名字的大小写 将一个人名存储到一个变量中，再以小写  大写 和首字母大写的方式显示人名
2-5 找一个名人说的名言。 将这个名人的姓名和他的名言打印出来。输出 xxx说过 xxxxxx
2-6 将名人的姓名存储在变量famous_person中，在创建要显示的消息。并将其存储在变量message中。然后打印这条消息
2-7 剔除人名中的空白，存储一个人名 开头 和末尾 都包含一些空白字符 务必使用到\t和\n
打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip()  rstrip() strip()对人名进行处理。并将结果打印出来
"""
user_name = "zhang san"
message = "你好吗:" + user_name
print(message)

name = "zhang san"
print(name.lower())
print(name.upper())
print(name.title())

mingyan = "好好学习\n天天向上"
name = "毛泽东"
print(name + "说过：" + mingyan)

mingyan = "好好学习\t天天向上"
name = "毛泽东"
message = name + "说过：" + mingyan
print(message)

name = " kaitou"
name1 = "kaitou "
name2 = " kaitou "
print(name.lstrip())
print(name1.rstrip())
print(name2.strip())