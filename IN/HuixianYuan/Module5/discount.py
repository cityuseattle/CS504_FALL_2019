sneakers={'name':'Fire Jordan', 'price':800}

def discount_price(product, discount):
    newprice=(product['price']*(1.0-discount))
    assert(0<=newprice<=product['price']), "Discount price is lower than zero."
    return newprice

print(discount_price(sneakers, 0.5))
print(discount_price(sneakers, 2))