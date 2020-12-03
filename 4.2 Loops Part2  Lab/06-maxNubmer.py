max_num = -100000000

while True:
  try:
    current = int(input())
    if max_num < current:
      max_num = current
  except:
    print(max_num)
    break


'''
-10
20
-30
'''



