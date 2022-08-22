## calculator trial

def inp():
    num1 = int(input("give the first number\n")) 
    num2 = int(input("give the second number\n"))
    return num1, num2

def sum(num1, num2):
    return num1+num2

def ext(num1, num2):
     return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2




cont="y"
inp()
num1= inp[1]
while cont == "y":
    
    print ("1- sum")
    print ("2- ext")
    print ("3- mult")
    print ("4- div")

    oper=0

    


    while oper != 1 or 2 or 3 or 4:
        oper = int(input("choose the operation: "))
        if oper == 1 or 2 or 3 or 4:
            break    
    
        
    if oper == 1:
        print(sum(num1,num2))
    if oper == 2:
        print(ext(num1,num2))
    if oper == 3:
        print(mult(num1,num2))
    if oper == 4:
        print(div(num1,num2))        
        
        
    cont = input("continue (y) / (n) ?")
        
        
        