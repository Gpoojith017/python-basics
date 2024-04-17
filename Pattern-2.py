n=int(input())
for i in range(n):
    for j in range(i):
        if i%2==0:
            print("*",end=" ")
        elif i%2!=0:
            print("#",end=" ")
    print()
