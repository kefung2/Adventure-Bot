monsterList = [
   {
    "name": "red",
    "hp": "10",
    "atk": "1",
    "deff": "1",
    "spd": "1",
    "exp": "1"
  },
  {    
    "name": "red",
    "hp": "10",
    "atk": "1",
    "deff": "1",
    "spd": "1",
    "exp": "1"
  },
  {    
    "name": "red",
    "hp": "10",
    "atk": "1",
    "deff": "1",
    "spd": "1",
    "exp": "1"
  }
]

class newMonster:
  def __init__(self,num):
    self.name = monsterList[num]['name']
    self.hp = int(monsterList[num]['hp'])
    self.curhp = int(monsterList[num]['hp'])
    self.atk = int(monsterList[num]['atk'])
    self.deff = int(monsterList[num]['deff'])
    self.spd = int(monsterList[num]['spd'])
    self.exp = int(monsterList[num]['exp'])
    
  def showStat(self):
    return(
      f"Name : {self.name}\n"
      f"HP : {self.curhp} / {self.hp}\n"
      f"ATK : {self.atk}\n"
      f"DEF : {self.deff}\n"
      f"SPD : {self.spd}"
      )
  
  def takeDamage(self, damage):
    self.curhp = self.curhp - damage
    return(f"You taken -{damage} damage")


  def isDead(self):
    return(self.curhp <= 0)