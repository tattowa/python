class Yusya:
    def __init__(self, job, name, damage):
        self.job = job
        self.name = name
        self.damage = damage

    def attack(self):
        print(self.job + "の" + self.name + "は、魔王に" + self.damage + "のダメージを与えた！")


party = []
party.append(Yusya("勇者", "ヨシヒコ", "100"))
party.append(Yusya("魔法使い", "ヒトミ", "50"))
party.append(Yusya("踊り子", "タクヤ", "20"))

for i in party:
    i.attack()
