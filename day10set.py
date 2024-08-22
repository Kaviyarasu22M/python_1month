a={1,2,3,4,5}
a.add(6)
print(a)

b={3,2,5,1}
c=b.intersection()
print("intersection",c)

e=a.issuperset(b)
print(e)

a.remove(5)
print("remove",a)

f=a.difference(b)
print(f)

g=a.isdisjoint(b)
print(g)

n=a.pop()
print(n)

s=sorted(b)
print("sort",b)

v=a.copy()
print("v",v)

h=a.union(b)
print("union",h)

