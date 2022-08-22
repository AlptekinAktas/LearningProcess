dupList2 = [5,5,5,5,5,4,4,4,4,3,3,3,2,2,1]
uniques = []

for number in dupList2:
    if number not in uniques:
        uniques.append(number)
    print(uniques)