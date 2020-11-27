days, chefs, cakes, gof, pancake = [int(input()) for _ in range(5)]
all_products = ((cakes * 45) + (gof * 5.8) + (pancake * 3.2)) * chefs
print(all_products * days * 0.875)

