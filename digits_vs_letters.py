dict_Num = {
"0" : "Zero",
"1" : "One",
"2" : "Two",
"3" : "Three",
"4" : "Four", 
"5" : "Five",
"6" : "Six",
"7" : "Seven",
"8" : "Eight",
"9" : "Nine", 
"10" : "Ten",
"11" : "Eleven",
"12" : "Twelve",
"13" : "Thirteen",
"14" : " Fourteen ",
"15" : "Fifteen",
"16" : "Sixteen",
"17" : "Seventeen",
"18" : "Eighteen",
"19" : "Ninteen",
"20" : "Twenty"
}


while True:
    numbers = input("write a number: ")
    wrt =""
    for ord in numbers:
        wrt += dict_Num[ord] + ", "
    print (wrt)