#cleverLily
age, laundry_price, toys_price = int(input()), float(input()), int(input())
money_count, toys_count, brother_racket = 0, 0, 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_count += (10 * i)
        brother_racket += 1
    else:
         toys_count += 1

toys_count *= toys_price
subtotal = (toys_count + (money_count / 2)) - brother_racket
total = abs(subtotal - laundry_price)

print(f'Yes! {total:.2f}') if subtotal >= laundry_price else print(f'No! {total:.2f}')

#10, 170, 6
