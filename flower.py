from turtle import *
import random

M, B, m, b = 6, 2, 5, 3

x = input("花の数を1~10で入力してください")
try:
    x = float(x)
except:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
    x = 6
if x < 1 or x > 10:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
else:
    M = x


x = input("花の大きさを1~4で入力してください")
try:
    x = float(x)
except:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
    x = 2
if x < 1 or x > 4:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
else:
    B = x


x = input("花びらの数を3~10で入力してください")
try:
    x = float(x)
except:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
    x = 5
if x < 3 or x > 10:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
else:
    m = x


x = input("花びらの大きさを2~5で入力してください")
try:
    x = float(x)
except:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
    x = 3
if x < 2 or x > 5:
    print("正しい値が入力されませんでした")
    print("既定の値で実行します")
else:
    b = x


c = b

for i in range(int(M)):
    b = int(10*c+15*int(B))
    if i != 0:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        up()
        goto(x, y)
        down()
    for h in range(int(B)):
        co = ["red", "yellow", "blue", "Indigo",
              "green", "Purple", "Orange", "sky blue"]
        a = random.choice(co)
        for j in range(int(m)):
            color("brown", str(a))
            begin_fill()
            left(60)
            forward(b / 2)
            right(60)
            forward(b)
            right(60)
            forward(b / 2)
            right(60)
            forward(b / 2)
            right(60)
            forward(b)
            right(60)
            forward(b / 2)
            right(120)
            right(360 / m)
            end_fill()
        right(120/m)
        b -= 15
