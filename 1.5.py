def fibonacci(n):
  a=0
  b=1
  for i in range(n):
   print(a,end=" ")
   nextterm=a+b
   a=b
   b=nextterm
n=int(input())
fibonacci(n)
