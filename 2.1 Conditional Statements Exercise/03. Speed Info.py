n = float(input())
result = 0

if n <= 10:
    result = 'slow'
elif 10 < n <= 50:
    result = 'average'
elif 50 < n <= 150:
    result = 'fast'
elif 150 < n <= 1000:
    result = 'ultra fast'
elif n > 1000:
    result = 'extremely fast'

print(result)

# 49.5
