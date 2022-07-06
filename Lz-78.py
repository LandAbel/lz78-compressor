# - LZ78 kódoló-dekódoló
# A kódomba törekedtem a magyar nyelv használatára mert nem tudtam, hogy mennyire megengedett az angol használata 

def kodolo78(text):
    alapkö = dict() #Létrehozok egy könyvtárat/ avagy szótárat
    i = 0
    index = 1
    kszam = [] #létrehozok a számoknak egy listát
    kbetu = [] #létrehozok a betűknek egy listát
    while i < len(text): #Ameddig i kisebb mint a szöveg hossza addig müködik
        stringment = text[i] #Létrehozok egy változott ami a szöveg i-edik elemét tartalmazza
        ialapkö = 0 
        while stringment in alapkö: #Ameddig a stringment változó eleme/tartalmazza az alapkönytárnak addig fut
            ialapkö = alapkö[stringment] #Új változót hozok létre ahol az alapkönyvtár stringment részét tárolom el
            if (i == len(text) - 1): #Ha i egyenlő a szöveg hossza -1-el akkor a stringment változó üres változóként folytatja éltét
                stringment = " "
                break # Az if függvénynre csak eddig volt szükségünk ezért azt lezárjuk
            i += 1
            stringment = stringment + text[i] 
        kszam.append(ialapkö) #A kódolt számokhoz hozzáfűzzűk az indexelt alapkönyvtárat(aka ialapkö)
        kbetu.append(stringment[len(stringment) - 1]) 
        if (stringment not in alapkö):  #Amennyiben a menteni kivánt karakterlánc nincs az alapkönyvtárban az alapkönyvtár indexe egyenlő lesz az index értékével
            alapkö[stringment] = index
            index += 1
        i += 1 

    return kszam, kbetu, alapkö #A definiált függvény visszadja ezen értékeket 

z = [] #Létrehozok egy üres listát
def dekodolo78(kszam, kbetu, alapkö):
    i = 0
    while i < len(kszam): #Ameddig az i rövidebb mint a kódolt szám (kszám) 
        if (kszam[i] != 0): 
            z.append(list(alapkö.keys())[list(alapkö.values()).index(kszam[i])]) #A "z" listához hozzáfűzzűk ahol elöször kilistázom a kulcsokat majd az értékekt végül indexelem a kódólt szám i. tagját
        z.append(kbetu[i])
        i += 1
    return z

print('---'*7)
print('LZ78 Tömörítő algoritmus:')
print('---'*7)
#Kódólás bemeneti típusa
h = int(input('Írja be az 1-t ha szöveget és 2-t ha fájlt kíván tömöríteni: '))
print('---'*7)  #A felhasználótól bekérek egy számot amely eldönti az algoritmus futását
if h == 1: #Amennyiben a h értéke 1 a felhasználónak egy egyszerű szöveget kell megadnia
    stringkódra = input('Adja meg a tömöríteni kívánt szöveget: ')
elif h == 2:#Amennyiben a h értéke 2 a felhasználónak egy fálj nevet kell megadnia kiterjesztéssel(MacOS esetén mappa azonos fájlt)
    file = input('Adja meg a tömöríteni kívánt fájl nevét: ')
    with open(file, 'r') as f: #A kiválasztott fájlt beolvasom 
        stringkódra = f.read()
else: 
    print('Nem megfelelő bemenet típus')

#Ebben a szekcióban alkalmazom az korábban definiált függvényeket
print('---'*7)
print ('Bevitt szöveg:',stringkódra)#A fájl/szöveget elleörzés gyanánt kiíratom
[kszam, kbetu, alapkö] = kodolo78(stringkódra) #meghívom a korábbiakban definiált függvényt a beolvasott szövegre
a = [kszam, kbetu, alapkö]
print('---'*7)
print('A tömörített fájl létrehozva tömöritett.txt néven')
print('---'*7)
output = open('tömöritett.txt','w+') #A tömörített szövegnek létrehozok egy új szöveg fájlt írásra
output.write(str(a)) #Az "a" változót string formátumban beíratom az elözőleg létrehozott fájlba
print('Kódolt szöveg: ', end='')
i = 0
while i < len(kszam): #A kódolt szöveget olvasható módón kiíratom
    print ('{',kszam[i],':', kbetu[i],'}', end=' ')
    i +=1 
dekodolo78(kszam, kbetu, alapkö) #A függvény dekódolja a változóinkat
print('\r\n')
print('---'*7)
print('Dekódolt szöveg:', ''.join(z))



