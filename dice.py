from random import randint



# How to do random numbers
# How to enter commands in console in python program
#


winnings = 10
print("Hej")
print("You have {} kr".format(winnings))


#----------------
while True:
    n = raw_input("How much do you want to bet?:\n")
    n = int(n)
    if n == 0:
        break

    if n > winnings:
        print('whoa buddy')
        n = winnings

    # Print from import method
    dice = randint(1, 6)

    if dice >= 5:
        print('Bamboozle!')
        winnings = winnings - n
        print winnings

    if winnings <= 0:
        print('Loser!')
        break

    if dice < 5:
        winnings = n + winnings
        print winnings
#-------------



print("You left with {} kr".format(winnings))


