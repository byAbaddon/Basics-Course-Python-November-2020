min_num = 100000000

while True:
  try:
    current = int(input())
    if min_num > current:
      min_num = current
  except:
    print(min_num)
    break
