class newPlayer:
  
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
          "=====================================\n"
          )

  def takeDamage(self, damage):
    self.curhp -= damage
    return(f"You taken -{damage} damage")

  def isDead(self):
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