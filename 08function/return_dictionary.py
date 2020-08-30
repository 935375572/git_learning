# 返回字典
def build_person(fist_name, last_name):
    person = {"fist": fist_name, "last": last_name}
    return person


print(build_person("jim", "sab"))


def build_person(fist_name, last_name, age=""):
    person = {"fist": fist_name, "last": last_name}
    if age:
        person["age"] = age
    return person


print(build_person("jim", "sab"))
print(build_person("jim", "sab", 12))