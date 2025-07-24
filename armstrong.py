n=int(input("Enter a number: "))
sum=0
m=n
while m>0:
    r=m%10
    sum=sum+r**3
    m//=10
if n==sum:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")