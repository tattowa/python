line = int(input())
a = []
b = []

for i in range(line):
    c = input().split(" ")
    if c[0] == c[2]:
        a.append(c)
    elif c[1] == c[3]:
        b.append(c)
d = []
for i in range(len(a)):
    for j in range(len(b)):
        if int(b[j][0]) <= int(a[i][0]) <= int(b[j][2]) and int(a[i][1]) <= int(b[j][1]) <= int(a[i][3]):
            d.append([a[i][0], b[j][1]])
d.sort()
# print(d)

e = []
for i in range(len(d)):
    for j in range(len(d)):
        for k in range(len(d)):
            for l in range(len(d)):
                if i < j < k < l:
                    if d[i][0] == d[j][0] and d[i][1] == d[k][1] and d[j][1] == d[l][1] and d[k][0] == d[l][0]:
                        g = int(d[j][1])-int(d[i][1])
                        h = int(d[k][0])-int(d[i][0])
                        if g*h < 0:
                            g = -g
                        e.append(int(g*h))
e.sort()
# print(e)
print(e[0])
