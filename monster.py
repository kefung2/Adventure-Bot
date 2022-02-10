monsterList = [
   {
    "name": "Slime",
    "level" : 1,
    "hp": 5,
    "atk": 1,
    "deff": 1,
    "spd": 1,
    "critMod" : 0,
    "critDamage" : 0,
    "exp": 1
  },
  {    
    "name": "Skeleton",
    "level" : 2,
    "hp": 8,
    "atk": 2,
    "deff": 6,
    "spd": 3,
    "critMod" : .05,
    "critDamage" : .2,
    "exp": 2
  },
  {    
    "name": "Slime",
    "level" : 1,
    "hp": 3,
    "atk": 5,
    "deff": 1,
    "spd": 3,
    "critMod" : .2,
    "critDamage" : .1,
    "exp": 1
  },
  {
    "name": "Slime",
    "level" : 1,
    "hp": 3,
    "atk": 1,
    "deff": 10,
    "spd": 1,
    "critMod" : .01,
    "critDamage" : 3,
    "exp": 1
  },
  {
    "name": "Wolf",
    "level" : 2,
    "hp": 10,
    "atk": 5,
    "deff": 1,
    "spd": 6,
    "critMod" : .2,
    "critDamage" : .25,
    "exp": 2
  },
  {
    "name": "Werewolf",
    "level" : 3,
    "hp": 8,
    "atk": 6,
    "deff": 5,
    "spd": 5,
    "critMod" : .25,
    "critDamage" : .3,
    "exp": 3
  },
  {
    "name": "Zombie",
    "level" : 2,
    "hp": 9,
    "atk": 1,
    "deff": 1,
    "spd": 2,
    "critMod" : .1,
    "critDamage" : 2,
    "exp": 2
  },
  {
    "name": "Snake",
    "level" : 3,
    "hp": 10,
    "atk": 4,
    "deff": 3,
    "spd": 4,
    "critMod" : .2,
    "critDamage" : .5,
    "exp": 3
  },
  {
    "name": "Obake",
    "level" : 4,
    "hp": 4,
    "atk": 10,
    "deff": 2,
    "spd": 9,
    "critMod" : .05,
    "critDamage" : .5,
    "exp": 4
  },
  {
    "name": "Dragon",
    "level" : 5,
    "hp": 20,
    "atk": 10,
    "deff": 10,
    "spd": 10,
    "critMod" : .1,
    "critDamage" : 2,
    "exp": 5
  },
]

class NewMonster:
  def __init__(self,num):
    self.name = monsterList[num]['name']
    self.level = monsterList[num]['level']
    self.hp = monsterList[num]['hp']
    self.curhp = monsterList[num]['hp']
    self.atk = monsterList[num]['atk']
    self.deff = monsterList[num]['deff']
    self.spd = monsterList[num]['spd']
    self.critMod = monsterList[num]['critMod']
    self.critDamage = monsterList[num]['critDamage']
    self.exp = monsterList[num]['exp']
    
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