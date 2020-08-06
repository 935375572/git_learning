# return 返回值
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " +  last_name
    return  full_name

# 调用返回值的函数时，需要提供一个变量用于存储返回的值
message = get_formatted_name(first_name="zhang",last_name="san")
print(message)

# 返回字典
def build_person(fiit_name,last_name):
    person = {"fiit":"fiit_name","last":"last_name"}
    return person

message1 = build_person(fiit_name="zhang",last_name="san")
print(message1)


def city_country(city_name,guojia):
    chengshi_guojia  = city_name + " " + guojia
    return chengshi_guojia
message = city_country(city_name="南京",guojia="中国")
print(message)

def make_album(geshou_name,zhuanji_name):
    zidiansi = {"歌手":geshou_name,"专辑名":zhuanji_name}
    return zidiansi
message = make_album(geshou_name="张三",zhuanji_name="lisi")
message1 = make_album(geshou_name="张三",zhuanji_name="qwe")
message2 = make_album(geshou_name="张三",zhuanji_name="asd")
print(message)
print(message1)
print(message2)

# 增加一个可选参数  歌曲数
def make_album(geshou_name,zhuanji_name,gequshu=""):
    # if gequshu 是True  (有内容)
    if gequshu:
        zidiansi = {"歌手": geshou_name, "专辑名": zhuanji_name,"歌曲数":gequshu}
        return zidiansi
    else:
        zidiansi = {"歌手":geshou_name,"专辑名":zhuanji_name}
        return zidiansi
message = make_album(geshou_name="张三",zhuanji_name="lisi",gequshu="5")
message1 = make_album(geshou_name="张三",zhuanji_name="qwe")
message2 = make_album(geshou_name="张三",zhuanji_name="asd")
print(message)
print(message1)
print(message2)