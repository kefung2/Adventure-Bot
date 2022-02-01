class NewPlayer:
  
  def __init__(self):
    pass
    
  def __init__(self, name, hp, atk, deff, spd):
    self.name = name
    self.level = 1
    self.hp = hp
    self.curhp = hp
    self.atk = atk
    self.deff = deff
    self.spd = spd
    self.critMod = .1
    self.mobEncounter = 0
    self.shopEncounter = 0
    self.eventEncounter = 0
    self.exp = 0

  def showStat(self):
    return(
          "=====================================\n"
          f"Name : {self.name}\n"
          f"HP : {self.curhp} / {self.hp}\n"
          f"LV : {self.level}\n"
          f"ATK : {self.atk}\n"
          f"DEF : {self.deff}\n"
          f"SPD : {self.spd}\n"
          f"EXP : {self.exp}\n"
          #f"Encounter count : {self.encounter}"
          "=====================================\n"
          )

  def takeDamage(self, damage):
    print(f"called, taking {damage} damage")
    self.curhp -= damage
    return

  def isDead(self):
    print(f"HP: {self.curhp} / {self.hp}")
    return(self.curhp <= 0)

  def gainEXP(self, expPoint):
    self.exp += expPoint

  def encounterUp(self, typeOfEncounter):
    match typeOfEncounter:
      case 0:
        self.mobEncounter += 1
      case 1:
        self.shopEncounter += 1
      case 2:
        self.eventEncounter += 1
      case _:
        print("soomething is wrong")

  def getEncounter(self):
    return (
      f"You ran into monster {self.mobEncounter} times\n"
      f"You see {self.shopEncounter} shop on your journey\n"
      f"{self.eventEncounter} event happened "
      )

  def getEXP(self):
    return self.exp

  def getSPD(self):
    return self.spd

  def getATK(self):
    return self.atk

  def getDEF(self):
    return self.deff

  def getEXP(self):
    return self.exp

  def levelUp(self):
    self.level += 1
    self.hp += 1
    self.atk += 1
    self.deff += 1
    self.spd += 1
    self.exp -= 8

  def setAtk(self, update):
    self.atk += update

  def setDef(self, update):
    self.deff += update

  def setHp(self, update):
    
    self.curhp += update
    if(self.curhp > self.hp):
      self.curhp = self.hp