def solve_spiders (numHeads, numLegs):
    solution_found = False
    trial = 0
    for numSpiders in range (1, numHeads + 1):
        for numChicks in range (1, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totalLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
            trial += 1
            if totalLegs == numLegs:
                solution_found = True
                print ("---------------------------------")
                print ("number of pigs: " + str(numPigs))
                print ("number of chicks: " + str(numChicks))
                print ("number of spiders: " + str(numSpiders))
                print ("number of tries: " + str(trial))
                print ("---------------------------------")
                

#                return (numPigs, numChicks, numSpiders, trial)
            if not solution_found == True:
                print ("There is no Solution!")

        return (None, None, None,None)
    
    
def barnyard_spider ():
    heads = int (input("write number of heads: "))
    legs = int (input("write number of legs: "))
    pigs, chicks, spiders, trial = solve_spiders (heads, legs)
    
    if pigs == None:
         print ("There is no solution!")
    else:
        print ("Number of Pigs: " + str(pigs))
        print ("Number of Chicks: " + str(chicks))
        print ("Number of Spiders: " + str(spiders))
        print ("Number of Tries: " + str(trial))        
barnyard_spider ()