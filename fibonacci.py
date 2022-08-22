def fib (n):
    if n == 0 or n ==1:
        return 1
    else:
        return fib (n-1) + fib (n-2)

repeat = "y"

while repeat == "y":
    n = int(input ("give a number: "))
    print(fib(n))
    repeat = ""
    while repeat != "y" and repeat != "n":
        repeat = input ("Another try? y/n :")
        

