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
    "Value" : 2
  }
]

healingList = [
  {
    "itemName" : "Potion",
    "Value" : 1
  },

  {
    "itemName" : "Medkit",
    "Value" : 3
  }
]

class NewWeapon:
  def __init__(self,num):
    self.value = weaponList[num]['value']

class NewArmor:
  def __init__(self, num):
    self.value = armorList[num]['value']

class NewHealing:
  def __init__ (self ,num):
    self.value = healingList[num]['value']


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

