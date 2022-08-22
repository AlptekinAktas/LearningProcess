def organized_func_of_censoring (message):
    censoredWords= {
    "Hello" : "@#$!@",
     "How" : "*******",
     "What" : "$$$$" }
    text=""
    words = message.split (" ")
    for word in words:
        text += censoredWords.get(word, word) + " "
    return text


m = input ("> ")
t = organized_func_of_censoring (m)
print (t)

#words = message.split (" ")
#for word in words:
#    text += censoredWords.get(word, word) + " "
#print(text)

