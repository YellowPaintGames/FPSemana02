phrase=input("Frase: ")
phrase2=input("2ª Frase: ")
charset=set()
string=""
for chars in range(len(phrase.split())):
    if phrase.split()[chars]==phrase2.split()[chars]:
        charset.add(phrase.split()[chars])
for char in charset:
    string+=" "+char
print(string)