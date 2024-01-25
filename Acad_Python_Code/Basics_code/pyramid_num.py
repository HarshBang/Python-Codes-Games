for i in range(6):
    for j in range(i):
        print(i, end=' ')
    print('')

for i in range(1, 6+1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

i = 5
while i >= 1:
    j = 5
    while j > i:
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1