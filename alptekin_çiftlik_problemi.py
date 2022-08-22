#for x in range (1,10):
#    for y in range (1,10):
#        if x+3 ==15 and x + y == 5:
#            print(x, y)
            
#            
#for ph in range(1,21):
#    print (ph)
#    for ch in range (1,21):
#        print (ph, ch)
#        for cl in range (1,57):
#            for pl in range (1,57):
#                if ph + ch == 20 and (ph * 4) + (ch * 2) == 56:                                                    
#                
#                    print(ph)
#            else:
#                print("hata")
                
tri = 0
heads = int (input ("write number of heads: "))
legs = int (input ("write number of legs: "))

for ph in range (1,heads + 1):
    
    for ch in range (1, heads - ph + 1):
        tri += 1
        pl = ph *4
        cl = ch * 2
        
        
        if ph + ch == heads and pl + cl == legs:
    
            print (ph)
            print (tri)