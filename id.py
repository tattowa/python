a=1
b=a
print(id(a),id(b))
b=2
print(id(a),id(b))
b="str"
print(id(b))


c=[[1,2],[3,4]]
d=c.copy()
d[0][0]=0
print(c)
print(d)
print(id(c[0]),id(d[0]))


e=(1,2)
e[0]=0
