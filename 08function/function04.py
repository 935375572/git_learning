"""
传递列表
"""
def greet_users(names):
    for name in names:
        message = "hello," + name
        print(message)
liebiaos = ["张三","李四","王五"]
greet_users(liebiaos)

# 在函数中修改列表 需要打印的设计存在一个列表中  打印后移动到另一个列表中
def print_models(upprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移动到列表completed_models中
    :param upprinted_designs: 打印设计列表
    :param completed_models:  打印后移动到的列表
    :return:
    """
    while upprinted_designs:
        current_design = upprinted_designs.pop()

        print("printing model:" + current_design)
        completed_models.add(current_design)

def show_commpleted_models(completed_models):
    """
        显示打印好的所有模型
            param completed_models:
        :return:
    """
    for completed_model in completed_models:
            print(completed_model)

upprinted_designs = ["iPhone case","robot case","huawei case"]
completed_models = []

print_models(upprinted_designs,completed_models)
show_commpleted_models(completed_models)