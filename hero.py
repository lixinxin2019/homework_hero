class Hero:
    hp = 0
    power = 0
    name = ""

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("双方打平了")

    def speak_lines(self, name):
        if name == "timo":
            print("提莫队长正在待命")
        elif name == "police":
            print("见识一下法律的子弹")
        else:
            raise Exception("不存在该英雄")
