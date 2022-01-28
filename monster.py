monsterList = [
   {
    "name": "Slime",
    "hp": 10,
    "atk": 1,
    "deff": 1,
    "spd": 1,
    "exp": 1
  },
  {    
    "name": "red",
    "hp": 10,
    "atk": 1,
    "deff": 1,
    "spd": 1,
    "exp": 1
  },
  {    
    "name": "blue",
    "hp": 9,
    "atk": 1,
    "deff": 1,
    "spd": 1,
    "exp": 1
  }
]

class NewMonster:
  def __init__(self,num):
    self.name = monsterList[num]['name']
    self.hp = monsterList[num]['hp']
    self.curhp = monsterList[num]['hp']
    self.atk = monsterList[num]['atk']
    self.deff = monsterList[num]['deff']
    self.spd = monsterList[num]['spd']
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

  def getEXP(self):
    return self.exp
  
  def getSPD(self):
    return self.spd

  def getATK(self):
    return self.atk

  def getDEF(self):
    return self.deff