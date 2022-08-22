def solve ( numHeads, numLegs):
    trial=0
    for numP in range (0, numHeads+1):
        trial += 1
        numC = numHeads - numP
        totalLegs = 4 * numP + 2 * numC
        
        if totalLegs == numLegs:
            return (numC, numP, trial)
    return (None, None)       
def barnYard():
    heads = int(input ("write the number of heads: "))
    legs = int(input ("write the number of legs: "))
    pigs, chickens, trial = solve (heads, legs)
    
    if pigs == None:
        print ("there is no solution!")
    else:
        print ("number of pigs: " + str(pigs) )
        print ("number of chickens: " + str(chickens) )        
        print ("number of trials: " + str (trial))
barnYard()