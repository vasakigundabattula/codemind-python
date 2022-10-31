n=int(input())
s=int(input())
p=0
q=0
for i in range(1,n):
    if n%i==0:
        p+=i
for j in range(1,s):
    if s%j==0:
        q+=j
if n==q and s==p:
    print("Amicable")
else:
    print("Not Amicable")
        

