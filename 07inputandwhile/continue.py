"""
continue 跳出当前循环到循环的开始
"""
current = 1
while current <= 10: # 小于等于10进入循环体
    current += 1 # 1+1 = 2
    if current % 2 == 0: # 如果2除以2=0 到开头开始
        continue
    else:
        print(current)
