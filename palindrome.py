def palindrome1 (s):
    print (s)
    if len(s) <=1:
        print ("able to reach zero point")
        return True
    else:
        return s[0] == s[-1] and palindrome1(s[1:-1])
        

word= (input ("check if this is a palindrome: "))
print ("word s0 - s-1", word[0:-1])
print ("word s1 - s-1", word[1:-1])

palindrome1 (word)
