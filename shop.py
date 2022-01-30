weaponList = [
  {
    "itemName" : "Dagger",
    "value" : 1
  },

  {
    "itemName" : "Knife",
    "value" : 1
  },

  {
    "itemName" : "Sword",
    "value" : 2
  },

  {
    "itemName" : "Pan",
    "value" : 2
  },

  {
    "itemName" : "Greatsword",
    "value" : 3
  }

]

armorList = [
  {
    "itemName" : "Shirt",
    "value" : 1
  },

  {
    "itemName" : "Shorts",
    "value" : 1
  },
  
  {
    "itemName" : "Pan for the booty",
    "value" : 1
  },

  {
    "itemName" : "Helmet",
    "value" : 2
  },

  {
    "itemName" : "Small Shield",
    "value" : 3
  },
  
]

healingList = [
  {
    "itemName" : "Herb",
    "value" : 1
  },

  {
    "itemName" : "Bandage",
    "value" : 2
  },

  {
    "itemName" : "Healing Potion",
    "value" : 4
  },

  {
    "itemName" : "Great Potion",
    "value" : 6
  },

  {
    "itemName" : "Med-kit",
    "value" : 20
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
      "=====================================\n"
      f"Pick one of the items to go with your adventure\n"
      f"1-Weapon : {self.name1} , increase attack by {self.atk} \n"
      f"2-Armor : {self.name2} , increase defense by {self.deff} \n"
      f"3-Healing : {self.name3} , recover HP by {self.heal} \n"
      "=====================================\n"
      
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

