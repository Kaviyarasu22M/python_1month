a={"name":"kavin","age":20}
print("dicitinary",a)
print("access:",a['name'])

print("add key value pair")
a["reg"]=22
print("add",a)

m=a.keys()
print("kays:",m)

n=a.values()
print("values:",n)

v=a.items()
print("item",v)

b={"college":"grt"}
a.update(b)
print("update",a)

j=a.get("name")
print("get",j)

a.clear()
print("clear",a)

f=b.copy()
print("copy",b)

t={"native":"akm"}
l={"no":22}
print("two dictinary merge")
t.update(l)
print("merge",t)
