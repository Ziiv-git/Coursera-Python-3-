inventory = [("shoes", 12, 29.99), ("shirts", 20, 9.99), ("sweatpants", 25, 15.00), ("scarves", 13, 7.75)]

for item in inventory:
    items = item[0]
    quantity = item[1]
    price = item[2]
    print('The store has {} {}, each for {} USD.'.format(quantity,items,price))
