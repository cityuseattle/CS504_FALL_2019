sneakers = {'name': 'fire Jordan', 'price': 800}

def discount_price(product, discount):
    newPrice = int(product['price'] * (1.0 - discount))

    assert (0 <= newPrice <= product['price']), "Discount price is lower than 0"
    return newPrice

print(discount_price(sneakers, 0.5))
print(discount_price(sneakers, 2))