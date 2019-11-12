import random


booleanData = "yes"
#Chooses a 4 digit random number
randoNumber =random.randint(1000, 9999)
print(randoNumber)
#Puts the random number into an array of integers
num = randoNumber
list2 = [int(x) for x in str(num)]

while booleanData.lower() == "yes":
    userinput = input("Guess a Random Number between 1000 and 9999")
    if int(userinput) != randoNumber:
        print("Shocker, you are wrong")
        #Puts the user input into an array of integers
        list1 = [int(x) for x in str(num)]
        for eachlet in list1:
            for everylet in list2:
             if eachlet == everylet:
                if list1.index == list2.index(eachlet):
                    print("You've done it")
                elif list1.index != list2.index(eachlet):
                    print(list2.index(eachlet))


    elif int(userinput) == randoNumber:
            print("Congratulations")
            booleanData = input("Would you like to play again? ")
            if booleanData.lower() == "yes":
                randoNumber =random.randint(1000, 9999)
                print(randoNumber)
                list2 #need a new li














    







