# create a random  number
import random

go_on = "y"
while go_on == "y":


    max= int(input("give a maximum number: "))
    number = random.randint(1,max)
    guess = None
    
    cnt_mx = int(max/2)
    for count in range(1,cnt_mx+1):
        if guess != number:
            guess =int(input("%s / %s Guess: " % (count, cnt_mx)))
            if guess == number:
                print ("Nice Guess" )
            if guess < number:
                print ("high" )
            if guess > number:
                print ("low" )

    if count ==  cnt_mx and guess != number:
        go_on = input("no more chances \ another guess? y / n ?" )
        
    if count == cnt_mx and guess == number:
        go_on =input ("congradulations! another guess? y / n ? ")
        
#if guess  is less then RN, say ..... 
#if guess  is more then RN, say ..... 
#if guess  is equel to RN, break
#add +1 to guess count
#if guess cont is 5, end