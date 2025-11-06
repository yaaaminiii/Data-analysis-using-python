t1=(10,60,30,40,50)
t2=('apple','banana','orange')
t3=(40,'apple',[10,20,30])
print(t1)
print(t2)
print(t3)
print(type(t1))
#single number in a tuple
t=(10,)
print(type(t))
print(t1[-1])
print(t1[2:4])#it prints from 2 to 3 excluding 4
print(t1[::1])#it prints from 0 index to 1 index
print(t1[4:6])
t4=t1+t #addition
print(t4)
# functions of tuple
#1.length of the tuple
print(len(t1))
#2.to count how many times it repeats
print(t1.count(10))
#3.to find the index
print(t1.index(10))
#4.to sort the elements
t5=sorted(t1)
print(t5)
#5.to print min element
print(min(t1))
#6.to check whether it exists
print(10 in t1)
#7.max element in tuple
print(max(t1))
#sum and average of the elements in the tuple
t6=eval(input())
l=len(t6)
total=0
for x in t6:
  total=total+x
print(total)
print(total/l)



