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
  def __init__(self, item1, item2, item3):
    
    a = weaponList[item1]
    b = armorList[item2]
    c = healingList[item3]



    print(f"printing list a {a}")
    print(f"printing list b {b}")
    print(f"printing list c {c}")

    self.shop = {
      0:a,
      1:b,
      2:c

    }

  def showValue(self):
    return(
      "================================\n"
      "Pick one of the following items\n"
      f"1- Weapon : {self.shop[0]['itemName']} , increase attack by {self.shop[0]['value']}\n"
      f"2- Armor : {self.shop[1]['itemName']} , increase defense by {self.shop[1]['value']}\n"
      f"3- Healing : {self.shop[2]['itemName']} , health recover by {self.shop[2]['value']}\n"

    )

  def getItem(self, index ):
    print(self.shop[index])
    return self.shop[index]


  def getAttack(self):
    return self.shop[0]['value']

  def getDeffence(self):
    return self.shop[1]['value']

  def getRecovery(self):
    return self.shop[2]['value']


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

