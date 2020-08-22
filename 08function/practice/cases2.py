def make_shirt(chima, ziyang):
    print("尺码是： " + str(chima) + " 字样是： " + ziyang)

make_shirt(chima=23, ziyang="我爱你中国")


def make_shirt(chima, ziyang="我爱你日本省"):
    print("尺码是： " + str(chima) + " 字样是： " + ziyang)

make_shirt(chima="大号") # 尺码大号 默认字样
make_shirt(chima="中号") # 尺码中号 默认字样
make_shirt(chima="中号", ziyang="我爱你台湾省") # 尺码中号 其他字样