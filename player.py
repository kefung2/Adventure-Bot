class NewPlayer:
  
  def __init__(self):
    pass
    
  def __init__(self, name, hp, atk, deff, spd):
    self.name = name
    self.hp = hp
    self.curhp = hp
    self.atk = atk
    self.deff = deff
    self.spd = spd
    self.encounter = 0
    self.exp = 0

  def showStat(self):
    return(
          "=====================================\n"
          f"Name : {self.name}\n"
          f"HP : {self.curhp} / {self.hp}\n"
          f"ATK : {self.atk}\n"
          f"DEF : {self.deff}\n"
          f"SPD : {self.spd}\n"
          f"EXP : {self.exp}\n"
          f"Encounter count : {self.encounter}"
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

  def encounterUp(self):
    self.encounter += 1

  def getEncounter(self):
    return self.encounter

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