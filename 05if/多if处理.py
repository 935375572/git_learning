"""
if - elif - else 功能很强大  但仅适用于只有一个条件满足的情况下。后面讲不在执行

多 if  多个条件为true 都执行。 都是独立。
"""
pisas = ["猪肉","牛肉","鱼肉"]
if "鱼人" in pisas:
    print("猪肉馅的披萨")
if "牛肉" in pisas:
    print("牛肉馅的披萨")
if "鱼肉" in pisas:
    print("鱼肉馅的馅饼")