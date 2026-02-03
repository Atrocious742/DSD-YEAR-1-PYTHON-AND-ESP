def calculate_final_price(price):
    if price > 100:
        discount = 0.20
    elif price >= 50:
        discount = 0.10
    else:
        discount = 0

    final_price = price - (discount * price)
    return final_price


price = 100
print(calculate_final_price(price))