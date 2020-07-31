"""
rstrip:去除右边的空白字符
lstrip:去除左边的空白字符
strip:去除两端的空白字符
"""

# rstrip:去除右边的空白字符
message = "hello "
print(message)
xiugaihoudemessage = message.rstrip()  # 将对message处理后的结果赋值给xiugaihoudemessage
print(xiugaihoudemessage)

# lstrip:去除左边的空白字符
name = " zhangsan"
print(name)
xiugaihoudename = name.lstrip()  # 将对name处理后的结果赋值给xiugaihoudename
print(xiugaihoudename)

# strip:去除两端的空白字符
biubiubiui = " beibigou "
print(biubiubiui)
ooo = biubiubiui.strip()  # 将对biubiubiui处理后的结果赋值给ooo
print(ooo)
