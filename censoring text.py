censoredWords= {
"Hello" : "@#$!@",
 "How" : "*******",
 "What" : "$$$$" }

text=""
message = input ("> ")
words = message.split (" ")
for word in words:
    text += censoredWords.get(word, word) + " "
print(text)