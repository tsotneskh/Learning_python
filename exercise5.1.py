try:
    price = float(input("ყიდვის თანხა (ლარი): "))
    promo_code = input("შეიყვანეთ პრომო კოდი. თუ არ გაქვთ - Enter: ")
    promo_code = promo_code.lower()

    if price >= 200:
        discount = 20 
    elif price >= 100:
        discount = 10   
    elif price >= 50:
        discount = 5   
    else:
        discount = 0
    
    final_price = price - price * discount / 100

    if promo_code == "vip": 
        final_price = final_price - 5
        if final_price <0:  
            final_price = 0
        print(" VIP კოდი: დამატებით -5 ლარი")

    print(f"ფასდაკლება: {discount}%\nგადასახდელი: {(final_price):.2f} ლარი")

except ValueError:
    print("თანხის შესაყვანად გამოიყენეთ მხოლოდ ციფრები: ")
