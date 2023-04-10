destination = input()

while destination != 'End':
    budget = float(input())
    money = 0

    while budget > money:
        tips = float(input())
        money += tips

    print(f'Going to {destination}!')
    destination = input()


  #--------------------------------------------------(2)---------------- TODO 8-test fail

[print(f'Going to {x}!') for x in iter(input, 'End') if x.isalpha()]
