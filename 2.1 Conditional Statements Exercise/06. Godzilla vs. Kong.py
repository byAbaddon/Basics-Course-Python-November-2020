budget, statist, clothes = [float(input()) for x in range(0,3)]
decors = budget / 10
clothes_sum = statist * clothes

if statist > 150:
    clothes_sum-= clothes_sum / 10

budget-= decors + clothes_sum

if budget >= 0:
    print(f'Action!\nWingard starts filming with {budget:.2f} leva left.')
else:
  print(f'Not enough money!\nWingard needs {abs(budget):.2f} leva more.')



