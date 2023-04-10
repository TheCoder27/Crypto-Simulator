import random
import time

# price variables
bitcoinPrice = 15000.00
etheriumPrice = 300.00
dogecoinPrice = 0.20

# User variables
money = 10
amtBitcoin = 0
amtEtherium = 0
amtDogecoin = 0  


# Functions
def buy():
    global amtBitcoin, amtDogecoin, amtEtherium, money, bitcoinPrice, etheriumPrice, dogecoinPrice

    buyChoice = input("Do you want to buy: Bitcoin, Etherium, or Dogecoin \n")
    if(buyChoice.lower() == "bitcoin"):
        amount = float(input("How much: "))
        if(money >= amount * bitcoinPrice):
            amtBitcoin += amount
            money -= amount * bitcoinPrice
            print("You gained " + str(amount) + " of bitcoin \n")
        else:
            print("You can not afford that. \n")
    elif(buyChoice.lower() == "etherium"):
        amount = float(input("How much: "))
        if(money >= amount * etheriumPrice):
            amtEtherium += amount
            money -= amount * etheriumPrice
            print("You gained " + str(amount) + " of etherium \n")
        else:
            print("You can not afford that. \n")
    elif(buyChoice.lower() == "dogecoin"):
        amount = float(input("How much: "))
        if(money >= amount * dogecoinPrice):
            amtDogecoin += amount
            money -= amount * dogecoinPrice
            print("You gained " + str(amount) + " of dogecoin \n")
        else:
            print("You can not afford that. \n")
    else:
        print("That is not an option \n")


def sell():
    global amtBitcoin, amtDogecoin, amtEtherium, money, bitcoinPrice, etheriumPrice, dogecoinPrice

    sellChoice = input("What do you want to sell: bitcoin, etherium, dogecoin: \n")
    if(sellChoice.lower() == "bitcoin"):
        if(amtBitcoin > 0):
            amount = float(input("How much would you like to sell: "))
            if(amount >= amtBitcoin):
                money += amount * bitcoinPrice
                amtBitcoin -= amount
                print("You sold " + str(amount) + " bitcoin \n")
            else:
                print("You do not have that much bitcoin \n")
        else:
            print("You do not have any dogecoin")
    elif(sellChoice.lower() == "etherium"):
        if(amtDogecoin > 0):
            amount = float(input("How much would you like to sell: "))
            if(amount >= amtEtherium):
                money += amount * etheriumPrice
                amtEtherium -= amount
                print("You sold " + str(amount) + " etherium \n")
            else:
                print("You do not have that much etherium \n")
        else:
            print("You do not have any dogecoin")
    elif(sellChoice.lower() == "dogecoin"):
        if(amtDogecoin > 0):
            amount = float(input("How much would you like to sell: "))
            if(amount >= amtDogecoin):
                money += amount * dogecoinPrice
                amtDogecoin -= amount
                print("You sold " + str(amount) + " dogecoin \n")
            else:
                print("You do not have that much dogecoin \n")
        else:
            print("You do not have any dogecoin")
    else:
        print("That is not an option \n")


def rest(dayToRest):
    while(dayToRest > 0):
        dayToRest -= 1
        priceChange()
        time.sleep(1)

def priceChange():
    global bitcoinPrice, etheriumPrice, dogecoinPrice

    bitcoinPrice += round(random.uniform(-2000, 2000), 2)
    etheriumPrice += round(random.uniform(-150, 150), 2)
    dogecoinPrice += round(random.uniform(-0.05, 0.05), 2)

    if(bitcoinPrice < 0):
        bitcoinPrice = 0

    if(etheriumPrice < 0):
        etheriumPrice = 0
        
    if(dogecoinPrice < 0):
        dogecoinPrice = 0

    print("\nBitcoin price: $" + str(bitcoinPrice) + ", You have - " + str(amtBitcoin))
    print("Etherium price: $" + str(etheriumPrice) + ", You have - " + str(amtEtherium))
    print("Dogecoin price: $" + str(dogecoinPrice) + ", You have - " + str(amtDogecoin) + "\n\n")


while(True):
    priceChange()
    print("Your money: " + str(money) + "\n")  
    Option = input("You can: buy, sell, or rest \n")

    if(Option.lower() == "buy"):
        buy()
    if(Option.lower() == "sell"):
        sell()
    if(Option.lower() == "rest"):
        resting = int(input("\nHow many days would you like to rest: "))
        rest(resting)
    else:
        pass