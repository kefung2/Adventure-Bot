import os
import discord
import monster
import player
import shop
import random
from keep_alive import keep_alive

client = discord.Client()

#the global var
gameState = False
curMob = None
curShop = None
curPlayer = None


def helpMenu():
    return ("Coming Soon \n" "Please wait")


def endgame():
    global curPlayer
    global gameState

    del curPlayer

    gameState = False
    curMob = None
    curShop = None
    curPlayer = None


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

    # Commend to start the game
    if msg.startswith('$start'):
        global gameState
        gameState = True
        await sendBack("Starting")
        await sendBack("Play story")
        print(gameState)

    #following commend only work if the game has begin
    if bool(gameState):
    #if True:
        # Commend to see menu
        if msg.startswith('$newPlayer'):
            statList = msg.split()
            for i in range(2, len(statList)):
                statList[i] = int(statList[i])
            print(statList)
            #print(message.author)
            if statList[2] + statList[3] + statList[4] + statList[5] > 20:
                await sendBack("stat too high")
            elif statList[2] + statList[3] + statList[4] + statList[5] < 20:
                await sendBack("you still have stat point to use")
            elif statList[2] + statList[3] + statList[4] + statList[5] == 20:
                global curPlayer
                curPlayer = player.newPlayer(statList[1], statList[2],
                                             statList[3], statList[4],
                                             statList[5])
                stat = curPlayer.showStat()
                await sendBack(stat)

        # Commed to move / go next
        if msg.startswith('$move'):
            if curPlayer == None:
                await sendBack("Please create a Charater first")
            else:
                if curPlayer.encounter == 10:
                    await sendBack("Thank you for playing!")

                if random.randint(0, 100) % 2 == 0:
                    await sendBack("You have encounter a monster")
                    #TO-DO: ADD BOSS AFTER 10 ENCOUNTER
                    #pending boss fight
                    curPlayer.encounter += 1
                    #print(curPlayer.encounter)
                    monsterIndex = random.randint(0,
                                                  len(monster.monsterList) - 1)
                    #print(monsterIndex)
                    global curMob
                    curMob = monster.newMonster(monsterIndex)
                    stat = curMob.showStat()
                    await sendBack(stat)
                else:
                    await sendBack("You have encounter a merchant")
                    curPlayer.encounter += 1
                    

        # Commend to fight
        if msg.startswith('$fight'):
            if curMob == None:
                await sendBack("There is no monster to fight")
            else:
                print("Checking Speed")
                print(curPlayer.spd > curMob.spd)
                # Check who have higher speed to go first
                if curPlayer.spd > curMob.spd:
                    playerDamage = curPlayer.atk - curMob.deff
                    #if Monster Defend is too high, you will always do 1 damage and vice versa
                    print("Damage: ", playerDamage)
                    if playerDamage < 0:
                        playerDamage = 1
                    curMob.takeDamage(playerDamage)
                    if curMob.isDead():
                        await sendBack("You killed the monster")
                        #global curMob
                        curPlayer.exp = curPlayer.exp + curMob.exp
                        del curMob
                        curMob = None
                    else:
                        monsterDamage = curMob.atk - curPlayer.deff
                        if monsterDamage < 0:
                            monsterDamage = 1
                        curPlayer.takeDamage(monsterDamage)
                        if curPlayer.isDead():
                            await sendBack("YOU ARE DEAD!!!")
                            endgame()

                else:
                    monsterDamage = curMob.atk - curPlayer.deff
                    if monsterDamage < 0:
                        monsterDamage = 1
                    curPlayer.takeDamage(monsterDamage)
                    if curPlayer.isDead():
                        await sendBack("YOU ARE DEAD!!!")
                        endgame()
                    playerDamage = curPlayer.atk - curMob.deff
                    #if Monster Defend is too high, you will always do 1 damage and vice versa
                    if playerDamage < 0:
                        playerDamage = 1
                    curMob.takeDamage(playerDamage)
                    if curMob.isDead():
                        await sendBack("You killed the monster")
                        curPlayer.exp = curPlayer.exp + curMob.exp
                        global curmob
                        del curMob
                        curMob = None

        # Commend to run from fight
        if msg.startswith('$run'):
            menu = helpMenu()
            await sendBack(menu)

        # Commend to buy item
        if msg.startswith('$buy'):
            try:
                item = int(msg.split("$buy", 1)[1])
                await sendBack(item)
            except:
                await sendBack("Please pick 1 item only")

        # Commend to see current monster stat
        if msg.startswith('$monStat'):
            menu = helpMenu()
            await sendBack(menu)

        #commend to see yoour stat
        if msg.startswith('$stat'):
            stat = curPlayer.showStat()
            await sendBack(stat)
            print(stat)

        # Comment to reset everything
        if msg.startswith('$reset'):
            menu = helpMenu()
            await sendBack(menu)

        # Commend to end the game
        if msg.startswith('$end'):
            #global gameState
            gameState = False
            await sendBack("Ending")
            print(gameState)
    else:
        await sendBack(
            "Please check the menu with $help first before starting the game")


keep_alive()
client.run(os.environ['TOKEN'])
