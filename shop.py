weaponList = [
  {
    "itemName" : "Dagger",
    "value" : 1
  },

  {
    "itemName" : "Sword",
    "value" : 2
  },

  {
    "itemName" : "Lance",
    "value" : 3
  }

  
]

armorList = [
  {
    "itemName" : "Cape",
    "value" : 1
  },
  
  {
    "itemName" : "Helmet",
    "value" : 2
  },

  {
    "itemName" : "Shield",
    "value" : 3
  }
  
]

healingList = [
  {
    "itemName" : "Bandage",
    "value" : 1
  },

  {
    "itemName" : "Potion",
    "value" : 3
  },

  {
    "itemName" : "Med-kit",
    "value" : 5
  }

]

class NewShop:
  def __init__(self, atk, deff, heal):
    
    self.name1 = weaponList[atk]['itemName']
    self.name2 = armorList[deff]['itemName']
    self.name3 = healingList[heal]['itemName']
    self.atk = weaponList[atk]['value']
    self.deff = armorList[deff]['value']
    self.heal = healingList[heal]['value']

  def showValue(self):
    return(
      f"Pick one of the items to go with your adventure\n"
      f"1-Weapon : {self.name1} , increase attack by {self.atk} \n"
      f"2-Armor : {self.name2} , increase defense by {self.deff} \n"
      f"3-Healing : {self.name3} , recover HP by {self.heal} \n"
      
    )
  
  def getAttack(self):
    return self.atk

  def getDeffence(self):
    return self.deff

  def getRecovery(self):
    return self.heal


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

