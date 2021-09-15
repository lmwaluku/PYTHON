import random

print('Generate Code')

codes = '0123456789'
count = 1
variables = 8

for c in range(count):
    value = ''
    for d in range(variables):
        value += random.choice(codes)
print(value)