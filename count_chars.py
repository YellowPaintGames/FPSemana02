phrase=input("Frase: ")
charcount={}
for chars in phrase:
    if chars in charcount:
        charcount[chars]=charcount[chars]+1
    else:
        charcount[chars]=1
print(charcount)