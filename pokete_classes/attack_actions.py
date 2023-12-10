"""Contains the AttackActions class"""

import time
from .weather import Weather


class AttackActions:
    """This class contains all actions callable by an attack
    All these methods belong to one or more attacks and follow the following
    pattern:
        ARGS:
            obj: The Poke object that attacks
            enem: The Poke object that is attacked
            providers: List of the current providers"""

    @staticmethod
    def cry(_, enem, __):
        """Cry attack action"""
        enem.miss_chance += 1

        time.sleep(1.5)
        enem.ico.map.outp.outp(f"{enem.name}'s {AttackActions.action_effect(miss_chance_increase=True)}!")

    @staticmethod
    def eye_pick(_, enem, __):
        """Eye pick attack action"""
        enem.miss_chance += 2

        time.sleep(1.5)
        enem.ico.map.outp.outp(f"{enem.name}'s {AttackActions.action_effect(miss_chance_increase=True)}!")

    @staticmethod
    def chocer(_, enem, __):
        """Chocer attack action"""
        enem.atc -= 1

        time.sleep(1.5)
        enem.ico.map.outp.outp(f"{enem.name}'s {AttackActions.action_effect(atc_increase=False)}!")

    @staticmethod
    def snooze(_, enem, __):
        """Snooze attack action"""
        enem.miss_chance += 0.5
        enem.atc -= 1
        enem.defense -= 1

        time.sleep(1.5)
        enem.ico.map.outp.outp(f"{enem.name}'s {AttackActions.action_effect(miss_chance_increase=True,atc_increase=False,def_increase=False)}!")

    @staticmethod
    def politure(obj, _, __):
        """Politure attack action"""
        obj.defense += 1
        obj.atc += 1

        time.sleep(1.5)
        obj.ico.map.outp.outp(f"{obj.name}'s {AttackActions.action_effect(atc_increase=True, def_increase=True)}!")
        

    @staticmethod
    def bark_hardening(obj, _, __):
        """Bark hardening attack action"""
        obj.defense += 1

        time.sleep(1.5)
        obj.ico.map.outp.outp(f"{obj.name}'s {AttackActions.action_effect(def_increase=False)}!")

    @staticmethod
    def dick_energy(obj, _, __):
        """Dick energy attack action"""
        obj.atc += 2

        time.sleep(1.5)
        obj.ico.map.outp.outp(f"{obj.name}'s {AttackActions.action_effect(atc_increase=True)}!")

    @staticmethod
    def hiding(obj, _, __):
        """Hiding attack action"""
        obj.defense += 2

        time.sleep(1.5)
        obj.ico.map.outp.outp(f"{obj.name}'s {AttackActions.action_effect(def_increase=False)}!")

    @staticmethod
    def brooding(obj, _, __):
        """Brooding attack action"""

        if obj.hp + 2 <= obj.full_hp:
            obj.hp += 2

            time.sleep(1.5)
            obj.ico.map.outp.outp(f"{obj.name}'s {AttackActions.action_effect(def_increase=False)}!")
        else:
            obj.hp += 0

    @staticmethod
    def heart_touch(_, enem, __):
        """Heart touch attack action"""
        enem.defense -= 4

        time.sleep(1.5)
        enem.ico.map.outp.outp(f"{enem.name}'s {AttackActions.action_effect(def_increase=False)}!")

    @staticmethod
    def super_sucker(obj, enem, _):
        """Super sucker attack action"""
        enem.hp -= 2
        obj.hp += 2 if obj.hp+2 <= obj.full_hp else 0

        time.sleep(1.5)
        obj.ico.map.outp.outp(f"{obj.name} absorbed {enem.name}'s HP")

    @staticmethod
    def sucker(obj, enem, __):
        """Sucker attack action"""
        enem.hp -= 1
        obj.hp += 1 if obj.hp+1 <= obj.full_hp else 0

        time.sleep(1.5)
        obj.ico.map.outp.outp(f"{obj.name} absorbed {enem.name}'s HP")

    @staticmethod
    def rain_dance(obj, _, providers):
        """Rain dance attack action"""
        providers[0].map.weather = Weather("rain")

        time.sleep(1.5)
        obj.ico.map.outp.outp("It started raining!")
        

    @staticmethod
    def encouragement(obj, _, providers):
        """Encouragement attack action"""
        for poke in next(
            prov for prov in providers if prov.curr == obj
        ).pokes[:6]:
            poke.atc += 2

            time.sleep(1.5)
        obj.ico.map.outp.outp(f"{obj.name}'s {AttackActions.action_effect(atc_increase=True)}!")

    @staticmethod
    def action_effect(miss_chance_increase = None, atc_increase = None, def_increase = None, hp_increase = False):
        """This method not used in rain_dance, super_sucker, sucker action"""
        miss_chance_effect = {
            miss_chance_increase : "accuray increased",
            not(miss_chance_increase) : "accurcy decreased",
            miss_chance_increase == None : ""
        }[True]
        attack_effect = {
            atc_increase : "attack increased",
            not(atc_increase) : "attack decreased",
            atc_increase == None : ""
        }[True]
        defense_effect = {
            def_increase : "defense increased",
            not(def_increase) : "defense decreased",
            def_increase == None : ""
        }[True]
        hp_effect = {
            hp_increase : "hp recovered",
            not(hp_increase) : ""
        }[True]

        effect_list = [miss_chance_effect, attack_effect, defense_effect, hp_effect]
        effect = ""
        for s in effect_list:
            if s != "":
                if effect == "":
                    effect += s
                else:
                    effect += (", " + s)

        return effect

if __name__ == "__main__":
    print("\033[31;1mDo not execute this!\033[0m")
