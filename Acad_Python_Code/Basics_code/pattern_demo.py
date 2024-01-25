rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print('')

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print('')

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if(j%2==1):
            print("*", end=' ')
        else:
            print("#",end=' ')    

    print('')


rows = 5
# It is used for number of spaces
k = 2 * rows - 2    
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("")


n = 5  
m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ')  
    print(" ")  


rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i, -1, -1):
        print(i, end=' ')
    print()