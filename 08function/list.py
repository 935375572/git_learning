# 传递列表
def greet_user(names): # 接收一个名字列表 存到形参names中 names = username
    for name in names:
        msg = "你好啊：" + name
        print(msg)

username = ["张三", "李四"]
greet_user(username)


# 3D打印公司 需要打印的设计存储在一个列表中   打印后移动到另一个列表中
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计。直到没有未打印的设计为止
    打印每个设计后，都将其移动到列表  completed_models中
    :param unprinted_designs: 未印出的设计
    :param completed_models: 完成的设计
    :return:
    """
    while unprinted_designs:
        current = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("打印模式" +current)
        completed_models.append(current)

def show_completed_models(completed_models):
    """
    显示打印好的模型
    :param completed_models:
    :return:
    """
    for completed_model in completed_models:
        print(completed_model)

# 创建列表
unprinted_designs = ["iphone cases", "xiaomi"]
completed_models = []

print(unprinted_designs, completed_models)
print_models(unprinted_designs[:], completed_models )   # 如果还想保留unprinted_designs 原始的数据  就使用[:] 副本   但尽量避免这样。 提高效率
show_completed_models(completed_models)

