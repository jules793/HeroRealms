#-------------------------------------------------------------------------------
# Name:        Hero Realms
# Purpose:     An attempt on creating a python code for a computer version of/
#              a board game "Hero Realms".
#
# Author:      Julia Szuminska
#
# Created:     02/06/2020
# Copyright:   (c) Julia 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import section
import random



# Format of the deck and cards:
# Deck is a dictionary containing cards. Cards are individual dictionaries containing all properties of a card.
# Example:
# deck = {'dragon': {'type':'imperial', 'cost': 5, 'damage': 8, 'gold':0, 'healing': 0}, ...}

starterDeck = {'dagger': {'type': 'default', 'damage': 1, 'gold':0, 'healing': 0}, \
               'shortsword': {'type': 'default', 'damage': 2, 'gold':0, 'healing': 0}, \
               'coin1': {'type': 'default', 'damage': 0, 'gold':1, 'healing': 0}, \
               'coin2': {'type': 'default', 'damage': 0, 'gold':1, 'healing': 0}, \
               'coin3': {'type': 'default', 'damage': 0, 'gold':1, 'healing': 0}, \
               'coin4': {'type': 'default', 'damage': 0, 'gold':1, 'healing': 0}, \
               'coin5': {'type': 'default', 'damage': 0, 'gold':1, 'healing': 0}, \
               'coin6': {'type': 'default', 'damage': 0, 'gold':1, 'healing': 0}, \
               'coin7': {'type': 'default', 'damage': 0, 'gold':1, 'healing': 0}, \
               'ruby': {'type': 'default', 'damage': 0, 'gold':2, 'healing': 0}}


# A function to create a deck based on file

def createDeckDict(filename):
    #Getting card information from a file, storing it in a list of lists
    with open(filename, 'r') as f:
        lines=f.readlines()
        splitLines= []
        for line in lines:
            splitLine = line.strip('\n').split(',')
            splitLines += [splitLine]

    #Putting card properties in a dictionary
    deckDict={}
    for line in splitLines:
        deckDict[line[0]] = {'type': line[5], 'cost': line[4], 'damage': line[1],\
        'gold': line[2], 'healing':line[3]}
    return deckDict

# A function to create a list with keys from a dictionary - this can be shuffled
def cardDictToL(givenD):
    cardNames = list(givenD.keys())
    return cardNames


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Settig up initial sets of cards

# starterDeck - a dictionary with initial cards

# starterDeckL - a list with names of inintial cards - can be shuffled
starterDeckL = cardDictToL(starterDeck)
print(starterDeckL)


#  deckD - a full deck dictionary
deckD = createDeckDict('cards.csv')

# deckL - a full deck list- can be shuffled
deckL = cardDictToL(deckD)

# EXTRA set - a dictionary with full deck, not to be touched!

saverDeck= createDeckDict('cards.csv')



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCTIONS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A function to shuffle cards, should take a set of cards- a list.

def shuffle(cardSet):
    random.shuffle()
    return cardSet


# Function definition: changeTurn()
# When called, the function moves on to the next player

def changeTurn(currentPlayer, turnEnded):
    if turnEnded == True:
        if currentPlayer == noOfPlayers:
            currentPlayer = 0
            return currentPlayer
        else:
            currentPlayer = currentPlayer + 1
            return currentPlayer
    else:
        print('Current turn is still active. Player ', currentPlayer, 'should play')
        print('If player ', currentPlayer, 'has finished, type: "END"')
        userInput = input('Type END to finish turn: ')
        if userInput == 'END':
            if currentPlayer == noOfPlayers:
                currentPlayer = 0
                return currentPlayer
            else:
                currentPlayer = currentPlayer + 1
                return currentPlayer
        else:
            print('Player ', currentPlayer, "'s turn")
            return currentPlayer


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Setting up player profiles: playerProfileSetUp


# variable deck must be a list
def playerProfileSetUp(noOfPlayers, health, deck):
    i=0
    playersValues={}
    while i <= noOfPlayers:
        nickname= str(input('Choose your name, player... '))
        playersValues[i] = {}
        playersValues[i]['name'] = nickname
        playersValues[i]['health']= health
        playersValues[i]['active cards']= []
        random.shuffle(deck)
        for card in deck:
            playersValues[i]['active cards'] += [card]
        playersValues[i]['discarded cards']= []
        i +=1
    return playersValues
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Pick a random card from deck.

def pickRandom(deck):
    cardToPick = random.choice(list(deck))
    #deleted = 0
    #for card in deck:
    #    if card == cardToPick:
    #        del card
    deck.remove(cardToPick)
    return cardToPick


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Update market

market=[]
def updateMarket(market,deck):
    while len(market)<5:
        newCard =pickRandom(deck)
        market = market + [newCard]
    return market

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Draw 5 cards from personal deck-active cards. Gives output: \
# [newdraw, newactive, newdiscarded]
# After using, set new card sets and print out 5 drawn cards.

def drawFive(activeCards, discardedCards):
    if len(activeCards) >= 5:
        newDraw = [activeCards[0:5]]
        activeCards = activeCards[5:]
        return [newDraw, activeCards, discardedCards]
    else:
        shuffle(discardedCards)
        activeCards = activeCards + discardedCards
        newDraw = [activeCards[0:5]]
        activeCards = activeCards[5:]
        discardedCards = []
        return [newDraw,activeCards, discardedCards]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Check if game finished, if any health <= 0

def checkIfEnd(playersProfiles):
    for player in playersProfiles:
        if playersProfiles[player]['health'] <= 0:
            loser = playersProfiles[player]['name']
            gameEnd(loser)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# End of the game function, when called, the game stops.

def gameEnd(loser):
    print(playersProfiles)
    print(loser, ' lost the game.')
    print('GAME OVER')
    gameEnded= True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GAMEPLAY
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Initial steps

# Asks for a number of players, subsracts 1 to count from 0.

#noOfPlayers = int(input('How many players?  ')) - 1
noOfPlayers=1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Asks for a value of health at the begining. Available values 20-100.

#startingHealth = int(input('What is the starting value of health? (20-100)  '))
#while startingHealth <20 or startingHealth > 100:
#    print('Incorrect value of starting health, try again.')
#    startingHealth = int(input('What is the starting value of health? (20-100)  '))
startingHealth=30
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Setting up player profiles

playersProfiles = playerProfileSetUp(noOfPlayers, startingHealth , starterDeckL)
print(playersProfiles)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Setting up market
market = updateMarket(market,deckL)
print( 'Cards in the market: ', market)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 2. Gameplay loop

gameEnded =False
currentPlayer=0
while gameEnded == False:
    print(playersProfiles[currentPlayer]['name'], "'s turn" )
    pickedCards = drawFive(playersProfiles[currentPlayer]['active cards'], playersProfiles[currentPlayer]['discarded cards'])[0]
    playersProfiles[currentPlayer]['active cards'] = drawFive(playersProfiles[currentPlayer]['active cards'],\
                                                     playersProfiles[currentPlayer]['discarded cards'])[1]
    playersProfiles[currentPlayer]['discarded cards'] = drawFive(playersProfiles[currentPlayer]['active cards'],\
                                                        playersProfiles[currentPlayer]['discarded cards'])[2]
    print(pickedCards)

    # Count gold
    goldCount=0
    for m in pickedCards:
        for card in m:
            if card in starterDeck:
                goldCount += starterDeck[card]['gold']
            else:
                goldCount += saverDeck[card]['gold']
    print('You have ', goldCount, ' gold to spend.')

    print('Market:')
    for card in market:
        print(card, saverDeck[card])

    print(market)
    # Buying

    cardToBuy = str(input('Which card do you want to buy? Type 0 if none.   '))

    while cardToBuy != '0':

        if cardToBuy not in market:
            print('Wrong input, try again.')
            cardToBuy = str(input('Which card do you want to buy? Type 0 if none.   '))
        else:
            price = saverDeck[cardToBuy]['cost']
            print ("card's price is", price)
            market.remove(cardToBuy)
            if int(price) <= goldCount:
                print ('Enough money!')
                playersProfiles[currentPlayer]['discarded cards'] +=  [cardToBuy]
                print(playersProfiles[currentPlayer]['discarded cards'])

                print (playersProfiles[currentPlayer]['name'], 'has bought', cardToBuy)
                goldCount = goldCount - int(price)
                print ('You now have ', goldCount, ' gold to spend.')
                cardToBuy = input('What card do you want to buy now? Type 0 if you have finished buying.   ')
            else:
                print("You don't have enough gold to buy", cardToBuy)
                cardToBuy = input('Chose a different card or type in 0 if finished.   ')

    # Count damage
    damageCount=0
    for m in pickedCards:
        for card in m:
            if card in starterDeck:
                damageCount += starterDeck[card]['damage']
            else:
                damageCount += saverDeck[card]['damage']
    print('You have ', damageCount, ' damage to use.')

    # Print health of all players
    i=0
    while i <= noOfPlayers:
        print(playersProfiles[i]['name'], 'is at', playersProfiles[i]['health'], 'health')
        i +=1

    # Use damage

    i=0
    while i <= noOfPlayers:
        if i != currentPlayer:
            print('How much damage for', playersProfiles[i]['name'], '?')
            damageGiven = int(input('How much damage?  '))

            playersProfiles[i]['health']= playersProfiles[i]['health'] - damageGiven
        i +=1


    # Print health of all players
    i=0
    while i <= noOfPlayers:
        print(playersProfiles[i]['name'], 'is at', playersProfiles[i]['health'], 'health')
        i +=1


    # Healing part
    # Counting healing

    healingCount=0
    for m in pickedCards:
        for card in m:
            if card in starterDeck:
                healingCount = 0
            else:
                healingCount += saverDeck[card]['healing']
    print('You have ', healingCount, ' healing to use.')
    # Use healing
    playersProfiles[currentPlayer]['health']= playersProfiles[currentPlayer]['health'] + healingCount


    # End of turn
    # print health
    i=0
    while i <= noOfPlayers:
        print(playersProfiles[i]['name'], 'is at', playersProfiles[i]['health'], 'health')
        i +=1

    # update market
    market = updateMarket(market,deckL)
    print( 'Cards in the market: ', market)

    # Check if anyone has lost
    i=0
    while i <= noOfPlayers:
        if playersProfiles[i]['health'] == 0:
            gameEnded=True
            print('Player', playersProfiles[i]['name'], 'has lost.')
            loserOfGame=str(playersProfiles[i]['name'])
        i +=1

    print('End of turn. ')
    quitGame = str(input('If you want to quit the game, type Q'))
    if quitGame == 'Q':
        gameEnded = True


gameEnd(loserOfGame)



