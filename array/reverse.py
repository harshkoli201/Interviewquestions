a = [5,4,3,2,1]
l = len(a)
s = 0 
e = l-1
while s<e:
    a[s],a[e] = a[e],a[s]
    s +=1
    e -=1
print(a)    