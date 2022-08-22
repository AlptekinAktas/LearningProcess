count=0
def fibonacci_calc(n):
    global count 
    count = count +1
    if n == 0 or n==1:
        return 1
    else:
        
        return fibonacci_calc(n-1) + fibonacci_calc(n-2)

def fibonacci_add(x):
    count_add=0
    l=[]
    for fib_num in range (0, x + 1):
        if fib_num <= n:
            count_add += 1
            l= l + [fibonacci_calc (fib_num)]
    return (l, count_add)



repeat = "y"
while repeat =="y":
    n = int(input("give a number to calculate:"))
    l, count_addd = fibonacci_add (n)
    print (l)
    print ("loops for calculating: ", count,"loops for listing", count_addd)
    count_addd=0
    count=0
    repeat= input("do you want to continue? y/n : ")
    while repeat != "y" and repeat!="n":
        repeat= input("do you want to continue? y/n : ")
        