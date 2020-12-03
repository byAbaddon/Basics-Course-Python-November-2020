total_sum = 0

while True:
   try:
      current_sum = float(input())
      if current_sum > 0:
         total_sum += current_sum
         print(f'Increase: {current_sum:.2f}')
      else:
         print(f'Invalid operation!\nTotal:', f'{total_sum:.2f}')
         break
   except:
      print('Total:', f'{total_sum:.2f}')
      exit()





