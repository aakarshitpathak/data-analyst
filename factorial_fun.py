def fact(n):
    if n==1:
        print(f"Factorial of {n} is 1 ")
    elif(n==0):
        print(f"Factorial of {n} is 0 ")
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)

a=int(input("Enter the number you want the factorial of: "))
fact(a)