dupList = [2,5,3,1,5,4,3,2,5,5,3,4,4,5,4]
print (dupList)
dupList.sort()
print (dupList)
dupList.reverse()
print (dupList)
for item in dupList:
    while dupList.count(item) > 1:
        dupList.remove(item)
        print (dupList)
    

