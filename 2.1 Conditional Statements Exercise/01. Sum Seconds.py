from datetime import datetime, timedelta

result = sum([int(input()) for _ in range(0,3)])
time = datetime(2020, 11, 1)
delta = timedelta(seconds = result)
print(str(delta)[slice(3, 10)])

