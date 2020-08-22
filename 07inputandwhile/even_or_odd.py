"""
判断奇数还是偶数
"""
shuzi = input("给我一个数字，我能告诉你是奇数还是偶数： ")
panduan = int(shuzi)
if panduan % 2 == 0:
    print("这是个偶数呢")
else:
    print("这是个奇数")