"""
如果被2整除 则不打印  结果是1  3  5  7  9
"""

current_number = 0
while current_number < 10:
    current_number+=1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)