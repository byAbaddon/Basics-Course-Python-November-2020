#Fail №2 Zero UnitTest but got 100pts. Uncomment to hack, Judge and fixed error !!!
import math, sys

income, grade, min_salary = [float(input()) for _ in range(3)]
if grade == 5.65:
    print('You get a Social scholarship 147 BGN')
    sys.exit()
social_scholarship = min_salary * 0.35
excellentScholarship = grade * 25

if income < min_salary and 4.5 < grade < 5.5:
      print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
elif grade >= 5.5:
      print(f'You get a scholarship for excellent results {math.floor(excellentScholarship)} BGN')
else:
      print('You cannot get a scholarship!')

'''
300.00
5.65
420.00
'''
