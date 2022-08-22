numbers = [999, 345, 3000,842,12, 356, 10020 ]
greater = 0
iteration =0
for number in numbers:
    greater =0
    for turn in range (len(numbers)):
        if number > numbers[turn]:
            greater +=1
            iteration +=1
    if greater == len(numbers)-1:
        print(number)
        print(iteration) 