m=int (input("Enter first number:"))
n=int (input("Enter second number:"))
if (m%n):
   (m,n)=(n,m%n)
   print(m,n)
else:
   gcd=n
   print (gcd)