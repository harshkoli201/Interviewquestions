a = [10,35,75,38]
n = len(a)
m = a[0]
for i in range (n):
    if a[i]>m:
        m = a[i]
print ("Largest Element in the array is = ",m)


a = [10,35,75,38]
n = len(a)
min = a[0]

for i in range (n):
    if a[i]<min:
        min = a[i]
print ("Smallest Element in the array is = ", min)
    
