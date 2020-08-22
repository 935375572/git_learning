"""
简单函数定义
"""
def greet_user():
    print("hello")
greet_user()

# greet_user("张三") 调用greet_user(username)，并在print函数中使用
# username是形参   实参是调用函数时传递给函数的信息。。将实参“Jesse”传递给了函数gree_user("jesse")中
def greet_user(username):
    print("hello"+ username)
greet_user("张三")
