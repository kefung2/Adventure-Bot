weaponList = [
  #attack, critR, critD
  {
    "itemName" : "Dagger",
    "id" : "atk",
    "value" : 1,
    "effect" : "Increase attack by 1"
  },

  {
    "itemName" : "Knife",
    "id" : "atk",
    "value" : 1,
    "effect" : "Increase attack by 1"
  },

  {
    "itemName" : "Sword",
    "id" : "atk",
    "value" : 3,
    "effect" : "Increase attack by 2"

  },

  {
    "itemName" : "Greatsword",
    "id" : "atk",
    "value" : 5,
    "effect" : "Increase attack by 3"

  },

  {
    "itemName" : "Hero's blade",
    "id" : "atk",
    "value" : 5,
    "effect" : "Increase attack by 5"

  },

  {
    "itemName" : "Kunais",
    "id" : "critR",
    "value" : 0.05,
    "effect" : "Increase crit rate by 5%"

  },

  {
    "itemName" : "Shurikens",
    "id" : "critR",
    "value" : 0.05,
    "effect" : "Increase crit rate by 5%"

  },

  {
    "itemName" : "Pan for wacking",
    "id" : "critD",
    "value" : 5,
    "effect" : "Increase crit damage by 5%"
   
  },

  {
    "itemName" : "Katana",
    "id" : "critD",
    "value" : 10,
    "effect" : "Increase crit damage by 10%"
  }

]

armorList = [
  #defense, resist, maxhp
  {
    "itemName" : "Shirt",
    "id" : "def",
    "value" : 1,
    "effect" : "Increase defense by 1"

    
  },

  {
    "itemName" : "Shorts",
    "id" : "def",
    "value" : 1,
    "effect" : "Increase defense by 1"

  },
  

  {
    "itemName" : "Helmet",
    "id" : "def",
    "value" : 2,
    "effect" : "Increase defense by 2"

  },

  {
    "itemName" : "Small Shield",
    "id" : "def",
    "value" : 3,
    "effect" : "Increase defense by 3"

  },

  {
    "itemName" : "Pan for the booty",
    "id" : "def",
    "value" : 3,
    "effect" : "Increase defense by 3"

  },

  {
    "itemName" : "Chainmail",
    "id" : "def",
    "value" : 5,
    "effect" : "Increase defense by 5"

  },

  {
    "itemName" : "Lucky charm",
    "id" : "maxHP",
    "value" : 1,
    "effect" : "Increase Max HP by 1"

  },

  {
    "itemName" : "Magical Bracelet",
    "id" : "maxHP",
    "value" : 3,
    "effect" : "Increase Max HP by 3"

  },

  {
    "itemName" : "Holy Armor",
    "id" : "maxHP",
    "value" : 5,
    "effect" : "Increase Max HP by 5"

  },
  
]

healingList = [
  #recover hp&mp, boost speed
  {
    "itemName" : "Herb",
    "id" : "heal",
    "value" : 1,
    "effect" : "HP recover by 1"

  },

  {
    "itemName" : "Bandage",
    "id" : "heal",
    "value" : 2,
    "effect" : "HP recover by 2"

  },

  {
    "itemName" : "Healing Potion",
    "id" : "heal",
    "value" : 4,
    "effect" : "HP recover by 4"

  },

  {
    "itemName" : "Great Potion",
    "id" : "heal",
    "value" : 6,
    "effect" : "HP recover by 6"

  },

  {
    "itemName" : "Med-kit",
    "id" : "heal",
    "value" : 20,
    "effect" : "HP recover by 20"

  },

  {
    "itemName" : "Strange pill",
    "id" : "Speed",
    "value" : 1,
    "effect" : "Increase speed by 1"
  },

  {
    "itemName" : "red-cow drink",
    "id" : "Speed",
    "value" : 3,
    "effect" : "Increase speed by 3"
  },


  {
      "itemName" : "Adrenaline",
      "id" : "Speed",
      "value" : 5,
      "effect" : "Increase speed by 5"
  },

#rng buffs

  {
      "itemName" : "Suspicious herb (Good luck)",
      "id" : "Speed",
      "value" : 5,
      "effect" : "Suddenly you feel hyper!! Increase speed by 10!!"
  },

  {
      "itemName" : "Suspicious herb (Good luck)",
      "id" : "Speed",
      "value" : -5,
      "effect" : "You started to feel sore... Decrease speed by -5"
  },


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
      1:a,
      2:b,
      3:c

    }

  def showValue(self):
    return(
      "================================\n"
      "Pick one of the following items\n"
      f"1- Weapon : {self.shop[1]['itemName']} , {self.shop[1]['effect']}\n"
      f"2- Armor : {self.shop[2]['itemName']} , {self.shop[2]['effect']}\n"
      f"3- Healing : {self.shop[3]['itemName']} , {self.shop[3]['effect']}\n"

    )

  def getItem(self, index ):
    print(self.shop[index])
    return self.shop[index]

  def getItemId(self, category):
    return self.shop[category]['id']
  
  def getItemValue(self, value):
    return self.shop[value]['value']

