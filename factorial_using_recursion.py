def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
num=int(input("Enter a positive number: "))
print(fact(num))
