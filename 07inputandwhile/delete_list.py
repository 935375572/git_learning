"""
删除包含特定值得所有列表元素
remove() 可以删除列表的特定值。 但是如果值重复。则只能删除第一个重复值
"""
pets = ["dog", "dog", "cat", "cat", "rabbit"]
while "cat" in pets:
    pets.remove("cat")

print(pets)