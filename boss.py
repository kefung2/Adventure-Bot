miniBossList = [
    {
        "name": "Gatekeeper",
        "level" : 999,
        "hp": 15,
        "atk": 2,
        "deff": 5,
        "spd": 5,
        "critMod" : 0.1,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "You shall not pass!! >:)",
    },
    {

    "name": "Guardian",
        "level" : 999,
        "hp": 5,
        "atk": 1,
        "deff": 20,
        "spd": 0,
        "critMod" : 0.1,
        "critDamage" : 2,
        "exp": 8,
        "message": "Turn back adventurer!!",
    },

    {

    "name": "Dark Knight",
        "level" : 999,
        "hp": 10,
        "atk": 5,
        "deff": 5,
        "spd": 15,
        "critMod" : 0.1,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "Lets duel",
    },

    {

    "name": "Unknown",
        "level" : 999,
        "hp": 20,
        "atk": 5,
        "deff": 0,
        "spd": 20,
        "critMod" : 0.5,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "Prepare to die!!",
    },

        ####Leave final boss teeto at the end for now
    {
        "name": "Final Boss Demonic Teeto",
        "level" : 999,
        "hp": 100,
        "atk": 10,
        "deff": 10,
        "spd": 100,
        "critMod" : 0.1,
        "critDamage" :.5,
        "exp": 8,
        "message": "Size doesnt mean anything~",
    },
    

]


class NewBoss:
    def __init__(self,num):
        self.name = miniBossList[num]['name']
        self.level = miniBossList[num]['level']
        self.hp = miniBossList[num]['hp']
        self.curhp = miniBossList[num]['hp']
        self.atk = miniBossList[num]['atk']
        self.deff = miniBossList[num]['deff']
        self.spd = miniBossList[num]['spd']
        self.critMod = miniBossList[num]['critMod']
        self.critDamage = miniBossList[num]['critDamage']
        self.exp = miniBossList[num]['exp']
        self.sentence = miniBossList[num]['message']

    def showStat(self):
        return(
            "=====================================\n"
            f"Name : {self.name}\n"
            f"HP : {self.curhp} / {self.hp}\n"
            f"ATK : {self.atk}\n"
            f"DEF : {self.deff}\n"
            f"SPD : {self.spd}\n"
            "=====================================\n"
            )


    def takeDamage(self, damage):
        self.curhp = self.curhp - damage
        return(f"You did -{damage} damage")


    def isDead(self):
        return(self.curhp <= 0)

    ## Getter / Setter
    def getLevel(self):
        return self.level

    def getEXP(self):
        return self.exp
    
    def getSPD(self):
        return self.spd

    def getATK(self):
        return self.atk

    def getDEF(self):
        return self.deff

    def getCritChance(self):
        return self.critMod*100
    
    def getCritDamage(self):
        return self.critDamage

    def showMessage(self):
        return(
            f"{self.sentence}"
        )
    