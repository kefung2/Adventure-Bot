class player:
  
  def __init__(self):
    pass
    
  def __init__(self, name, hp, mp, atk, deff, spd):
    self.name = name
    self.hp = hp
    self.curhp = hp
    self.mp = mp
    self.curmp = mp
    self.atk = atk
    self.deff = deff
    self.spd = spd

  def showStat(self):
    return(
          f"Name : {self.name}\n"
          f"HP : {self.curhp} / {self.hp}\n"
          f"MP : {self.curmp} / {self.mp}\n"
          f"ATK : {self.atk}\n"
          f"DEF : {self.deff}\n"
          f"SPD : {self.spd}"
          )
