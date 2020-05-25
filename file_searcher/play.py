

# Fibanacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibanacci(limit):
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current


print('with yield')
for n in fibanacci(100):
    if n > 1000:
        break
    
    print(n, end=', \n')