# 让实参变成可选的
def get_name(fist_name, last_name, zhongjianming=""):  # zhongjianming  中间名传一个空值  可选的
    if zhongjianming: # 非空代表true
        full_name = fist_name + zhongjianming + last_name
    else:
        full_name = fist_name + last_name
    return full_name


print(get_name(fist_name="张", last_name="三"))
print(get_name(fist_name="张", zhongjianming="小", last_name="三"))

