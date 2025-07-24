n=int(input("Enter a number: "))
m=n
rev = 0

while m>0:
    r=m%10
    rev=rev*10+r
    m=m//10

if n==rev:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")