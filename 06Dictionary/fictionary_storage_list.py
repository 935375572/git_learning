"""
字典存储列表
当需要在字典中 将一个键关联到多个值时。可以在字典中嵌套一个列表
披萨表皮和配料
"""
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
print("你点了一份" + pizza["crust"] + "的披萨") # you ordered a thick-crust pizza with the folowing toppings

for topping in pizza["toppings"]:
    print(topping)

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name , languages in favorite_languages.items():
    print(name.title() + "s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
