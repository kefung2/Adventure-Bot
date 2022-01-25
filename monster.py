monsterList = [
   {
    "name": "red",
    "hp": "10",
    "atk": "red",
    "deff": "asd",
    "spd": "asd"
  },
  {    
    "name": "red",
    "hp": "10",
    "atk": "red",
    "deff": "asd",
    "spd": "asd"
  },
  {    
    "name": "red",
    "hp": "10",
    "atk": "red",
    "deff": "asd",
    "spd": "asd"
  }
]

class newMonster:
  def __init__(self,num):
    self.name = monsterList[num].name
    self.hp = monsterList[num].hp
    self.curhp = monsterList[num].hp
    self.atf = monsterList[num].atk
    self.deff = monsterList[num].deff
    self.spd = monsterList[num].spd
    
  def showStat(self):
    return(
      f"Name : {self.name}\n"
      f"HP : {self.curhp} / {self.hp}\n"
      f"ATK : {self.atk}\n"
      f"DEF : {self.deff}\n"
      f"SPD : {self.spd}"
      )