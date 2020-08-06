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
        completed_models.append(current_design)

def show_commpleted_models(completed_models):
    """
        显示打印好的所有模型
            param completed_models:
        :return:
    """
    for completed_model in completed_models:
            print("设计好之后的列表：" + completed_model)

upprinted_designs = ["iPhone case","robot case","huawei case"]
completed_models = []

print_models(upprinted_designs,completed_models)
show_commpleted_models(completed_models)

# 如果想即便打印了所有的设计后，也要保留原来未打印的设计列表。可向函数传递副本
print_models(upprinted_designs[:],completed_models)