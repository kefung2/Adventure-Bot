miniBossList = [
    {
        "name": "Gatekeeper",
        "level" : 999,
        "hp": 10,
        "atk": 3,
        "deff": 5,
        "spd": 4,
        "critMod" : 0.10,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "You shall not pass!! >:)",
        "effects" : "Special effect : None"

    },
    {

    "name": "Guardian",
        "level" : 999,
        "hp": 3,
        "atk": 2,
        "deff": 50,
        "spd": 2,
        "critMod" : 0.10,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "Turn back adventurer!!",
        "effects" : "Special effect: Gains attack each turn"
    },

    {

    "name": "Dark Knight",
        "level" : 999,
        "hp": 10,
        "atk": 6,
        "deff": 5,
        "spd": 15,
        "critMod" : 0.3,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "Lets duel!",
        "effects" : "Special effect: Heals on hit"
    },

    {

    "name": "Unknown",
        "level" : 999,
        "hp": 10,
        "atk": 5,
        "deff": 5,
        "spd": 20,
        "critMod" : 0.2,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "Prepare to die!!",
        "effects": "Special effect: Destroy player's defense",
    },

    {
    "name": "Elementalist",  #testing
        "level" : 999,
        "hp": 20,
        "atk": 1,
        "deff": 5,
        "spd": 5,
        "critMod" : 0.1,
        "critDamage" : 0.5,
        "exp": 8,
        "message": "Feel the power of the elements!",
        "effects": "Special effect: Master of the four elements",
    },

        ####Leave final boss teeto at the end for now
    {
        "name": "Final Boss Demonic Teeto",
        "level" : 999,
        "hp": 30,
        "atk": 1,
        "deff": 20,
        "spd": 100,
        "critMod" : 0.30,
        "critDamage" :0.50,
        "exp": 8,
        "message": "Size doesnt mean anything~",
        "effects": "Special effect: LOOK OUT FOR SHROOMS!"
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
        self.effect = miniBossList[num]['effects']

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
            f"{self.sentence}\n"
            f"{self.effect}"
        )
    
    def getName(self):
        return self.name

    #scales boss stats on entrance
    def bossScaling(self, counterrate):
        if(counterrate > 11):
            print("scaling boss")
            #self.curhp += (round(counterrate))
            #self.hp += (round(counterrate))
            self.curhp = self.curhp*2
            self.hp = self.hp*2
            self.atk = (self.atk*2)
            self.deff = (self.deff*2)

    #for buffing during battle
    def buffBoss(self, stat, value):
        if (stat == 'hp'):
            if(self.curhp > 0):
                self.curhp += value
                if(self.curhp > self.hp):
                    self.curhp = self.hp

        if (stat == 'atk'):
            self.atk += value

        if (stat == 'def'):
            self.deff += value

        if (stat == 'speed'):
            self.spd += value

        if (stat == 'crit'):
            self.critMod += value

        if (stat == 'critdmg'):
            self.critDamage += value
