from police import Police
from timo import Timo


class HeroFactory:

    def create_hero(self, name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception("不存在该英雄")


hero_factory = HeroFactory()
timo = hero_factory.create_hero("timo")
police = hero_factory.create_hero("police")
timo.speak_lines("timo")
police.speak_lines("police")
timo.fight(police.hp, police.power)