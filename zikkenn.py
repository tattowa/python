line = int(input())
for i in range(line):
    a = input().split(" ")
    for j in range(len(a)):
        a[j] = str(a[j])
    if a[-1] == "s" or a[-1] == "o" or a[-1] == "x":
        a.append("es")
    elif a[-2:] == ["s", "h"] or a[-2:] == ["c", "h"]:
        a.append("es")
    elif a[-1] == "f":
        a.pop()
        a.append("ves")
    elif a[-2:] == ["f", "e"]:
        del a[-2:]
        a.append("ves")
    elif (a[-1] == "y") and (a[-2] != a or a[-2] != i or a[-2] != u or a[-2] != e or a[-2] != o):
        a.pop()
        a.append("ies")
    else:
        a.append("s")
    b = ("").join(a)
    print(b)
