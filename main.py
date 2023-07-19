n=int(input())
b=int(input())
c=""
while n>0:
    c=str(n%b)+c
    n//=b
print(c)
