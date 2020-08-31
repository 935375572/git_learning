def city_county(name, guojia):
    quanming = name + "," + guojia
    return quanming

full_name = city_county(name="南京", guojia="中国")
print(full_name)

def make_album(name, zhuanjiming, gequshu=""): # 接收歌手的姓名和专辑名
    geshou = {"姓名": name, "专辑名":zhuanjiming }
    if gequshu:
        geshou["歌曲数"] = gequshu;
    return geshou

while True:
    print("请输入一个专辑的歌手和名称")
    geshou = input("歌手是：")
    if geshou == "quit":
        break
    zhuanji_name = input("名称是：")
    if zhuanji_name == "quit":
        break
    lala = make_album(name=geshou, zhuanjiming=zhuanji_name)
    print(lala)

caiyilin = make_album(name="蔡依林", zhuanjiming="马德里不思议")
zhoujielun = make_album(name="周杰伦", zhuanjiming="七里香")
linjunjie = make_album(name="林俊杰", zhuanjiming="江南", gequshu=21)
print(caiyilin)
print(zhoujielun)
print(linjunjie)