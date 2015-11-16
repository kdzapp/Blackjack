import random
import time

ace = "Ace"
faceCards = ["King", "Jack", "Queen"]
cardSuit = ["Spades", "Hearts", "Diamonds", "Clubs"]
initalCash = 1000

def header():
    print "************************************"
    print "*********     Welcome     **********"
    print "*********       to        **********"
    print "*********    Blackjack    **********"
    print "************************************"
    
def ender():
    print
    print "***********************************"
    print "*********     Thanks     **********"
    print "*********       for      **********"
    print "*********     Playing    **********"
    print "***********************************"

def menu():
    print "\n              Menu               \n"
    print "1) Play Game"
    print "2) Settings"
    print "3) Exit Game\n"
    print "You have", initalCash, "$ in the bank"
def settings():
    print "\n             Settings               \n"
    print "1) Set Cash Amount"
    print "2) Return to Menu"

def getCard(val):
    
    if val <= 10:
        return val
    elif val <= 13:
        i = val % 3
        return faceCards[i]
    else:
        return ace
    
def optimizeAce(totalCards, size, currentTotal):
    aceCount = 0
    
    for n in range(size):
        if totalCards[n] == ace:
            aceCount += 1

    if aceCount == 0:
        return totalCards
    elif aceCount == 1:
        for n in range(size):
            if totalCards[n] == ace:
                if currentTotal <= 10:
                    totalCards[n] = 11
                else:
                    totalCards[n] = 1
        return totalCards
    else:
        for n in range(size):
            if totalCards[n] == ace:
                totalCards[n] = 1
        return totalCards

def calcMoney(bet, won):

    if won:
        netCash = initalCash + bet
        return netCash
    else:
        netCash = initalCash - bet
        return netCash

def calcTotalOfCards(totalCards, size):
    
        totalVal = 0
            
        #Calculates total of cards
        for n in range(size):
            for j in range(3):
                if totalCards[n] == faceCards[j]:
                    totalCards[n] = 10
            if totalCards[n] != ace:
                totalVal += int(totalCards[n])
        totalCards = optimizeAce(totalCards, size, totalVal)
        totalVal = 0
        for n in range(size):
            totalVal += totalCards[n]

        return totalVal

def aiTotal(card1, card2):
    count = 2
    allAiCards = [card1, card2]

    total = calcTotalOfCards(allAiCards, count)

    while total < 16:
        time.sleep(2)
        allAiCards.append(getCard(random.randint(1, 15)))
        total = calcTotalOfCards(allAiCards, count)
        count += 1
        print "\nDealer hits"
    
    print "\nDealer stays\n"

    print "Dealer's total is", total
    if total > 21:
        print "The Dealer busted!"
        return 0
    
    return total
        
def runGame():

    bet = int(raw_input("\nPlace Bet ($): "))
    
    print "You've bet", bet, "$"
    print "\nDealing..."
    #Get Random Numbers
    randomCard = random.randint(1, 15)
    randomCard2 = random.randint(1, 15)
    dCard1 = getCard(randomCard)
    dCard2 = getCard(randomCard2)
    
    print "\nDealer Card Showing:", dCard1
    randomCard = random.randint(1, 15)
    randomCard2 = random.randint(1, 15)

    userCard1 = getCard(randomCard)
    userCard2 = getCard(randomCard2)
    print "Your Cards:", userCard1, "and", userCard2
    
    while True:
        randomCards = [userCard1, userCard2]
        print "\nDouble, Stay or Hit?\n"
        userInput = raw_input(" =>  ")

        if userInput.lower() == "double":
            bet *= 2
            print "Your bet has been doubled..."
            print "Drawing card...\n"
            randomCard3 = random.randint(1, 15)
            userCard3 = getCard(randomCard2)
            print "You drew a", userCard3

            randomCards.append(userCard3)
            totalVal = calcTotalOfCards(randomCards, 3)
            
            #Prints total
            print "Your total:", totalVal
            break
        elif userInput.lower() == "stay":
            totalVal = calcTotalOfCards(randomCards, 2)
            print "\nOkay, your total is", totalVal
            break
        elif userInput.lower() == "hit":
            count = 3
            print "Drawing card...\n"
            randomCards.append(getCard(random.randint(1, 15)))
            print "You drew a", randomCards[count - 1]
            totalVal = calcTotalOfCards(randomCards, count)
            if totalVal < 21:
                print "Your current total:", totalVal
                print "\nStay or Hit?\n"
                userInput = raw_input(" =>  ")
            
                while True:
                    if userInput.lower() == "stay":
                        totalVal = calcTotalOfCards(randomCards, count)
                        print "\Okay, your is total:", totalVal
                        break
                    elif userInput.lower() == "hit":
                        print "Drawing card...\n"
                        randomCards.append(getCard(random.randint(1, 15)))
                        print "You drew a", randomCards[count]
                        totalVal = calcTotalOfCards(randomCards, count)
                        print "Your current total:", totalVal
                        count += 1
                        if totalVal > 21:
                            break
                break
            else:
                break
        else:
            print "Invalid Input"
        
    if totalVal > 21:
        money = calcMoney(bet, False)
        print "You busted!\n"
        print "Your new total is", money, "$"
        return money
    else:
        print "Dealer shows his card, it's a", dCard2
        aiCards = aiTotal(dCard1, dCard2)
        
        if aiCards < totalVal:
            money = calcMoney(bet, True)
            print "You've won!\n"
            print "Your new total is", money, "$"
            return money
        elif aiCards > totalVal:
            money = calcMoney(bet, False)
            print "You've lost...\n"
            print "Your new total is", money, "$"
            return money
        else:
            money = calcMoney(0, False)
            print "Push! There is no winner\n"
            print "Your total remains the same,", money, "$"
            return money
    
#Print Header
header()
menu()

menuVal = 0

while True:
    print
    userInput = int(raw_input("=> "))
    
    #Menu Conditional
    if userInput == 1:
        initalCash = runGame()
        menu()
    elif userInput == 2:
        settings()
        while True:
            print
            userInput = int(raw_input("=> "))

            if userInput == 1:
                initalCash = int(raw_input("Enter $ Amount: "))
                print "\nOkay, the dollar amount has been set to", initalCash, "$"
                menu()
                break
            elif userInput == 2:
                menu()
                break
            else:
                print "\nSorry, that's not a settings option..."
            
    elif userInput == 3:
        ender()
        break
    else:
        print "\nSorry, that's not a menu option..."
