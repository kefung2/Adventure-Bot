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