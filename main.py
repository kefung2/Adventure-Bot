import os
import discord
import monster
import player
import shop
import random
#from keep_alive import keep_alive
# import requests

# r = requests.head(url="https://discord.com/api/v1")
# try:
#     print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
# except:
#     print("No rate limit")

client = discord.Client()

#the global var
gameState = False
curMob = None
curShop = None
curPlayer = None
previousEnc = -1



def helpMenu():
    return (
        " - - - - - Menu - - - - -\n"
        "$start : Begin the game\n"
        "$newPlayer : Use the commend to create a new charater in the following order and stat should sum up to 20: $newPlayer [name] [hp] [attack] [defend] [speed] \n"
        "$move : move the charater forward with 50% chance of seeing a monster or merchant \n"
        "$fight : fight the monster\n"
        "$run : run away from the monster\n"
        "$buy : buy item in shop: $buy [item in slot]\n"
        "$monStat : see the current monster stat\n"
        "$stat : see your oown current stat\n"
        "$levelUp : Use this Comment to level up. Every 8 exp point give you a level, which give you more stat\n"
        "$reset : reset the whole world\n"
        "$end : end the game\n")


def playStory():
    return ("In the Kingdom of Hyakki, there is a princess name Ayame, who is crownd the most beautiful lady in the kingdom. One day the Demon King Teeto, has caught eye on the princess, and kidnap her away. The king has summon a hero from a different world in order to save his daughter. Now hero your jounery has begin.")


def endgame():
    global curPlayer, curMob, curShop, gameState, previousEnc

    del curPlayer

    gameState = False
    curMob = None
    curShop = None
    curPlayer = None
    previousEnc = -1


def checkPlayerCreation():
    if curPlayer == None:
        return False
    else:
        return True


def checkMobAlive():
    if curMob == None:
        print("false")
        return False
    else:
        print("true")
        return True

def playerDamagePhase(crit):
    playerDamage = curPlayer.getATK() - curMob.getDEF()
    #if Monster Defend is too high, you will always do 1 damage and vice versa
    print("Damage: ", playerDamage)
    if playerDamage < 0:
        playerDamage = 1
    if crit:
        playerDamage = round(playerDamage + (playerDamage * curPlayer.getCritDamage()))
    curMob.takeDamage(playerDamage)
    return playerDamage

def playerCritCheck():
    critChance = curPlayer.getCritChance()
    hit = random.randint(1, 100)
    print(f"Player crit roll {hit}; Chance {critChance}")
    if hit <= critChance:
        return True
    else:
        return False


def monsterDamagePhase(crit):
    monsterDamage = curMob.getATK() - curPlayer.getDEF()
    if monsterDamage < 0:
        monsterDamage = 1
    if crit:
        monsterDamage = round(monsterDamage + (monsterDamage * curMob.getCritDamage()))
    curPlayer.takeDamage(monsterDamage)
    return monsterDamage

def monsterCritCheck():
    critChance = curMob.getCritChance()
    hit = random.randint(1, 100)
    print(f"Monster crit roll {hit}; Chance {critChance}")
    if hit <= critChance:
        return True
    else:
        return False

def randomEncounter():
    roll = random.randint(1, 100)
    # global previousEnc
    # print(f"previousEnc = {previousEnc}")
    # 50%: monster (0), 30% shop (1), 20% random event (2)
    
    if roll > 50:
        print(roll, "mob")
        return 0
    elif 20 < roll <= 50:
        print(roll, "shop")
        return 1
    elif 1 <= roll <= 20:
        print(roll, "event")
        return 2

######################################################################################################

@client.event
async def on_ready():
    print('{0.user} Online'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # shorthand for code
    msg = message.content
    sendBack = message.channel.send

    # Commend to see menu
    if msg.startswith('$help'):
        menu = helpMenu()
        await sendBack(menu)
        return

    # Commend to start the game
    if msg.startswith('$start'):
        global gameState
        gameState = True
        await sendBack("Starting")
        story = playStory()
        await sendBack(story)
        await sendBack("Please tell us about yourself Hero")
        return
        #print(gameState)

    #following commend only work if the game has begin
    #if bool(gameState):
    if True:
        # Commend to see menu
        if msg.startswith('$newPlayer'):
            global curPlayer
            if not(curPlayer == None):
              await sendBack("I already know about you, Hero")
            else:
              try:
                  statList = msg.split()
                  for i in range(2, len(statList)):
                      statList[i] = int(statList[i])
                  print(statList)
                  #print(message.author)
                  if statList[2] + statList[3] + statList[4] + statList[5] > 20:
                      await sendBack("stat too high")
                  elif statList[2] + statList[3] + statList[4] + statList[5] < 20:
                      await sendBack("you still have stat point to use")
                  elif statList[2] + statList[3] + statList[4] + statList[
                          5] == 20:
                      curPlayer = player.NewPlayer(statList[1], statList[2],
                                                  statList[3], statList[4],
                                                  statList[5])
                      stat = curPlayer.showStat()
                      await sendBack(stat)
              except:
                  await sendBack(
                      "Please follow the format $newPlayer [name] [hp] [attack] [defend] [speed]"
                  )
                  return

        if bool(checkPlayerCreation()):
            # Commed to move / go next

            if msg.startswith('$move'):
                global curMob
                global curShop

                if not(curShop == None):
                    # remove shop if player decide to not buy anything and move on
                    await sendBack("You left without buying anything")
                    del curShop
                    curShop = None
                if bool(checkMobAlive()):
                    await sendBack(
                        "Monster is blocking your way, fight it or run from it"
                    )
                else:
                    if curPlayer.getEncounter() == 10:
                        endgame()
                        await sendBack("Thank you for playing!")
                    encounterType = randomEncounter()
                    if encounterType == 0:
                        await sendBack("You have encounter a monster")
                        #TO-DO: ADD BOSS AFTER 10 ENCOUNTER
                        #pending boss fight
                        curPlayer.encounterUp(0)
                        #print(curPlayer.encounter)
                        monsterIndex = random.randint(
                            0,
                            len(monster.monsterList) - 1)
                        #print(monsterIndex)
                        curMob = monster.NewMonster(monsterIndex)
                        stat = curMob.showStat()
                        await sendBack(stat)
                    elif encounterType == 1:
                        await sendBack("You have encounter a merchant")
                        curPlayer.encounterUp(1)
                        
                        item1 = random.randint(0, len(shop.weaponList) -1 )
                        item2 = random.randint(0, len(shop.armorList) -1 )
                        item3 = random.randint(0, len(shop.healingList) -1 )
                        curShop = shop.NewShop(item1, item2, item3)
                        values = curShop.showValue()
                        await sendBack(values)
                    elif encounterType == 2:
                        curPlayer.encounterUp(2)
                        await sendBack("Random event coming soon!")

                    
            # Commend to fight
            if msg.startswith('$fight'):
                if curMob == None:
                    await sendBack("There is no monster to fight")
                else:
                    print("Checking Speed")
                    # Check who have higher speed to go first
                    if curPlayer.getSPD() > curMob.getSPD():
                        crit = playerCritCheck()
                        playerDamage = playerDamagePhase(crit)
                        if crit:
                            await sendBack(f"You crited and did {playerDamage} damage")
                        else:
                            await sendBack(f"You did {playerDamage} damage")
                        if curMob.isDead():
                            await sendBack("You killed the monster")
                            curPlayer.gainEXP(curMob.getEXP())
                            expGain = curMob.getEXP()
                            await sendBack(f"You gain {expGain} exp")
                            stat = curPlayer.showStat()
                            await sendBack(stat)
                            del curMob
                            curMob = None
                            return
                        else:
                            crit = monsterCritCheck()
                            monsterDamage = monsterDamagePhase(crit)
                            await sendBack(
                                f"Monster fight back, and you took {monsterDamage} damage"
                            )
                            if curPlayer.isDead():
                                await sendBack("YOU ARE DEAD!!!")
                                endgame()
                                return
                    else:
                        crit = monsterCritCheck()
                        monsterDamage = monsterDamagePhase(crit)
                        await sendBack(
                            f"The Monster attack, and you took {monsterDamage} damage"
                        )
                        if curPlayer.isDead():
                            await sendBack("YOU ARE DEAD!!!")
                            endgame()
                            return
                        crit = playerCritCheck()
                        playerDamage = playerDamagePhase(crit)
                        await sendBack(
                            f"You fight back and did {playerDamage} damage back"
                        )
                        if curMob.isDead():
                            await sendBack("You killed the monster")
                            curPlayer.gainEXP(curMob.getEXP())
                            expGain = curMob.getEXP()
                            await sendBack(f"You gain {expGain} exp")
                            stat = curPlayer.showStat()
                            await sendBack(stat)
                            del curMob
                            curMob = None
                            return
                    try:
                      if not (curPlayer.isDead()) and not (curMob.isDead()):
                          stat1 = curPlayer.showStat()
                          await sendBack(stat1)
                          stat2 = curMob.showStat()
                          await sendBack(stat2)
                    except:
                        print("Player or Monster is dead") 
                        return

            # Commend to run from fight
            if msg.startswith('$run'):
                if curMob == None:
                    await sendBack("There is nothing to escape from...")

                else:
                    playerSpeed = curPlayer.getSPD()
                    monsterSpeed = curMob.getSPD()

                    playercounter = 0
                    monstercounter = 0

                    x = 0
                    y = 0
                    
                    while(playerSpeed > x):
                        rollvalue = random.randint(1,10)
                        #await sendBack(f"your speed is {playerSpeed}")
                        #await sendBack(f"i is {i}")
                        #await sendBack(f"you roll {rollvalue}")
                        if rollvalue > 8 :
                            playercounter += 1
                        #await sendBack(f"your final value {playercounter}")
                        x += 1

                    while(monsterSpeed > y):
                        rollvalue = random.randint(1,10)
                        #await sendBack(f"monster roll {rollvalue}")
                        if rollvalue > 8 :
                            monstercounter += 1
                        #await sendBack(f"monster final value {monstercounter}")
                        y += 1

                    if playercounter > monstercounter :
                        await sendBack("Successfully escape!")
                        del curMob
                        curMob = None

                    else:
                        await sendBack("Fail to escape!")
                        monsterDamage = monsterDamagePhase()
                        await sendBack(f"You took {monsterDamage} damage")
                        stat = curPlayer.showStat()
                        await sendBack(stat)
                        if curPlayer.isDead():
                            await sendBack("YOU ARE DEAD!!!")
                            endgame()

            # Commend to buy item
            if msg.startswith('$buy'):
                if(curShop == None):
                    await sendBack("There is nothing to buy, use $move to continue your journey")
                atkvalue=curShop.getAttack()
                defvalue=curShop.getDeffence()
                healvalue=curShop.getRecovery()


                try:
                    item = int(msg.split("$buy", 1)[1])
                    await sendBack(f"You chose item {item}")

                except:
                    await sendBack("Please pick 1 item only")

                if(item == 1):
                    await sendBack(f"Increase attack stat by {atkvalue}")
                    curPlayer.setAtk(atkvalue)
                    stat=curPlayer.showStat()
                    await sendBack(stat)
                    await sendBack("Good luck on your adventure")
                    del curShop
                    curShop = None
                    
                        
                if(item == 2):
                    await sendBack(f"Increase defense stat by {defvalue}")
                    curPlayer.setDef(defvalue)
                    stat=curPlayer.showStat()
                    await sendBack(stat)
                    await sendBack("Good luck on your adventure")
                    del curShop
                    curShop = None


                if(item == 3):
                    await sendBack(f"Hp increase by {healvalue}")
                    curPlayer.setHp(healvalue)
                    stat=curPlayer.showStat()
                    await sendBack(stat)
                    await sendBack("Good luck on your adventure")
                    del curShop
                    curShop = None

                

            # Commend to see current monster stat
            if msg.startswith('$monStat'):
                stat = curMob.showStat()
                await sendBack(stat)


            #commend to see yoour stat
            if msg.startswith('$stat'):
                stat = curPlayer.showStat()
                await sendBack(stat)

            #commend to see Level up
            if msg.startswith('$levelUp'):
                if curPlayer.getEXP() >= 8:
                    await sendBack("You level Up")
                    curPlayer.levelUp()
                    stat = curPlayer.showStat()
                    await sendBack(stat)
                else:
                    await sendBack("Not enough exp to level up")

            # Comment to reset everything
            if msg.startswith('$reset'):
                await sendBack("resetting...")
                endgame()
                global gamestate
                gameState = True

            # Commend to end the game
            if msg.startswith('$end'):
                #global gameState
                endgame()
                await sendBack("Ending")
                print(gameState)
        else:
            await sendBack("Please tell me about yourself")
    else:
        await sendBack(
            "Please check the menu with $help first before starting the game")


#keep_alive()
# client.run(os.environ['TOKEN'])
