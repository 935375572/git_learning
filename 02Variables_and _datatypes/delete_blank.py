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