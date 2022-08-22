import random
theBus=[]

currentstation = "beylikdüzü"
bus1= ["beylikdüzü","avcılar","küçükçekmece","cevizlibağ","zincirlikuyu"]
bus2= ["beylikdüzü","avcılar","küçükçekmece","cevizlibağ","zincirlikuyu"]
bus3= ["beylikdüzü","avcılar","küçükçekmece","cevizlibağ","zincirlikuyu"]
bus4= ["beylikdüzü","avcılar","küçükçekmece","cevizlibağ","zincirlikuyu"]
bus5= ["beylikdüzü","avcılar","küçükçekmece","cevizlibağ","zincirlikuyu"]
cont = "n"
time = 1
money= 100


while money > 0:
    while not cont == "y":
        theBus=[]
        wait = 0
        while not currentstation in theBus:
            wait = random.randint (1,5)        
            busNumber = random.randint (1,5)
            if busNumber ==1:
                theBus = bus1
            elif busNumber ==2:
                theBus = bus2
            if busNumber ==3:
                theBus = bus3
            if busNumber ==4:
                theBus = bus4
            if busNumber ==5:
                theBus = bus5
        print (f"You waited for {wait} minutes and this bus just arrived: {theBus[0]} - {theBus[-1]}")        
        time = time + wait
        cont=input('Will you take the bus? y/n ')    
    
    money -= 8            
                         
    inThebus = True   
    
         
    while inThebus:
        print (f"{time} minutes past from you started the journey and you have {money} TL left")
        print ("These are the options for the bus level:")
        print ("""
        1- see the current station
        2- go to the next station
        3- get off from the bus
        """)
        opt_inThebus = int(input ("What do you want to do?"))
        if opt_inThebus == 1:
           print(f"You are at the {currentstation} station now ")
           print(f"Next station is: {theBus[theBus.index(currentstation)+1]} ")
        elif opt_inThebus == 2:
           currentstation = theBus[theBus.index(currentstation)+1]
           print(f"You are at the {currentstation} station now ")
           time += 2           
        elif opt_inThebus == 3:     
           print(f"You got off from the bus in {currentstation}")
           cont = "n"
           inThebus = False
        else:
               oOıkOkkprint ("Sorry! I couldn't get it!")zaaazww22a