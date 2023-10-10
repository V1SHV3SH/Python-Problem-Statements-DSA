shop = []
while True:
    p = input("Please add an item to the shopping list ('q - quit )")
    if p=='q':
        break
    flag=False
    for i in shop:
        if i == p:
            flag = True
            break
    if flag:
        print("Item-"+p+"- is already in the shopping list")
    else:
        shop.append(p)
    shop.sort()
    print(shop)
