#dictionaries
d={}
d[100]="yamini"
d[200]="teju"
print(d)
print(d[100])
d={200:'teju'}

#updation
d[100]="sravya"
print(d)
print(d[100])
#to find out the length
print(len(d))

if 200 in d:
    print(d[200])
    
#DELETION 
del d[100]
print(d)
#to clear all the elements
d.clear()
print(d)
#addition
s1={"sub1":70,"sub2":80}
sum=0;
for x in s1:
    sum+=s1[x]
print(sum)

#to delete entire dict
del(d)

d1={}
d1[100]="yamini"
d1[200]="teju"
print(d1)
#to get the element at 100
print(d1.get(100))
print(d1.popitem())
print(d1)


















