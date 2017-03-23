def price_plus_tax(item):
    nyc_tax = 0.08875
    # calculate just the tax on the item
    item_tax = item * nyc_tax
    # total is item price plus tax
    total = item + item_tax
    return total

print price_plus_tax(50)
