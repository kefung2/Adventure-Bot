weaponList = [
  {
    "itemName" : "Dagger",
    "Value" : 1
  },

  {
    "itemName" : "Sword",
    "Value" : 2
  }
]

armorList = [
  {
    "itemName" : "Shield",
    "Value" : 1
  },
  
  {
    "itemName" : "Helmet",
    "value" : 2
  }
]

healingList = [
  {
    "itemName" : "Potion",
    "value" : 1
  },

  {
    "itemName" : "Medkit",
    "value" : 3
  }
]

class NewShop:
  def __init__(self, atk, deff, heal):
    self.atk = weaponList[atk]['value']
    self.deff = armorList[deff]['value']
    self.heal = healingList[heal]['value']

  def showValue(self):
    return(
      f"attack : {self.atk}"
      f"defense : {self.deff}"
      f"healing : {self.heal}"
    )
    

"""
offName
offStat
defName
defSat
helName
helStat

getoff(num)
 return offStat

============================================
1- itemname : stat
2- itemname: stat
item 3 : stat

"""

