while True:
    try:
        age = int(input ("> "))
    except ValueError:
        print ("Value Error")