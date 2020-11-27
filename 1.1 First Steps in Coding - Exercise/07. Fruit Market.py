y, b, kgO, kgR, kgY = [float(input()) for _ in range(5)]
raspberries = y / 2
oranges = raspberries * 0.60
bananas = raspberries * 0.20
sumKgR = kgR * raspberries
semKgO = kgO * oranges
semKgB = b * bananas
semKgY = kgY * y

print(sumKgR + semKgO + semKgB  + semKgY)


