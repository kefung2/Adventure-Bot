item1name = None
item2name = None
item3name = None

item1value = None
item2value = None
item3value = None

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

    global item1name, item2name, item3name, item1value, item2value, item3value

    item1name = a['itemName']
    item2name = b['itemName']
    item3name = c['itemName']

    item1value = a['value']
    item2value = b['value']
    item3value = c['value']

    print(f"Item 1 name is {item1name}")

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
      f"1- Weapon : {item1name} , increase attack by {item1value}\n"
      f"2- Armor : {item2name} , increase defense by {item2value}\n"
      f"3- Healing : {item3name} , health recover by {item3value}\n"

    )

  def getItem(self, index ):
    print(self.shop[index])
    return self.shop[index]


  def getAttack(self):
    return item1value

  def getDeffence(self):
    return item2value

  def getRecovery(self):
    return item3value


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

