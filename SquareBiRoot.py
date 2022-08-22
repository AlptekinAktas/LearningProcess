def squareRootBi(x, epsilon):
    assert x > 0, "Must be a non-negative number, not " +str(x)
    assert epsilon > 0, "Must be a positve number, not " + str (epsilon)
    low = 0
    high = x
    guess = (low + high) / 2.0
    ctr = 1

    while abs (guess **2 - x) > epsilon and ctr <= 100:
        print (ctr, "- ", "low: ", low , "high: ", high, "guess: ", guess)
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        
        guess = (low + high) / 2.0
        ctr += 1
    assert ctr <= 100, "Iteration count exceeded"
    print ( 'Bi method. Number of iterations: ' , ctr, 'Estimate: ', guess)
    return guess

while True:    
    x = float(input("give a number to find square root: "))
    epsilon = float(input("give a number as epsilon: "))
    squareRootBi (x,epsilon)