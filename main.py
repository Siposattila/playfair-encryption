#! /usr/bin/env python3

# Ez a funckció eltávolítja az összes lehetséges space-t
def RemoveSpaces(string):
    for i in string:
        if i == ' ':
            i = ''
    return string

# Ha a szó hossza nem egyenletes vagyis nem osztója a 2 akkor hozzáadunk egy extra karaktert ebben az esetben a z lesz az
def Prepare(string):
    if len(string) % 2 != 0:
        string += 'z'
    return string

# Ezzel a funkcióval készítjük el az 5x5-ös két dimenziós kulcs táblánkat
def GenerateKeyTable(key, keyTable):
    j = 0
    i = 0

    for k in key:
        keyTable[i][j] = k
        j += 1
        if j == 5:
            i += 1
            j = 0
    
    k = 0
    while k < 5:
        keyTable[i][j] = chr(k + 97)
        j += 1
        if j == 5:
            i += 1
            j = 0
    return keyTable

# Ezzel a funkcióval keressük meg a digraph karaktereket és visszaadjuk a pozíciójukat
def SearchForDigraph(keyTable, a, b):
    digraphPosition = list()

    if a == 'j':
        a = 'i'
    if b == 'j':
        b = 'i'

    for i in 5:
        for j in 5:
            if keyTable[i][j] == a:
                digraphPosition[0] = i
                digraphPosition[1] = j
            elif keyTable[i][j] == b:
                digraphPosition[2] = i
                digraphPosition[3] = j
    return digraphPosition

# Funckció, ami elvégzi a titkosítást
def Encrypt(string, keyTable):
    i = 0

    while i < len(string):
        digraphPosition = SearchForDigraph(keyTable, string[i], string[i+1])

        if digraphPosition[0] == digraphPosition[2]:
            string[i] = keyTable[digraphPosition[0]][(digraphPosition[1] + 1) % 5]
            string[i + 1] = keyTable[digraphPosition[0]][(digraphPosition[3] + 1) % 5]
        elif digraphPosition[1] == digraphPosition[3]:
            string[i] = keyTable[(digraphPosition[0] + 1) % 5][digraphPosition[1]]
            string[i + 1] = keyTable[(digraphPosition[2] + 1) % 5][digraphPosition[1]]
        else:
            string[i] = keyTable[digraphPosition[0]][digraphPosition[3]]
            string[i + 1] = keyTable[digraphPosition[2]][digraphPosition[1]]

        i += 2
    return string

# A mindent elvégző funkció
def EncryptWithPlayfair():
    # Titkosítani kívánt szó bekérése a felhasználótól
    plaintext = input("Kérem írja be a titkosítani kívánt szót! \n")
    print("A titkosítani kívánt szó:", plaintext)

    # Titkosításhoz használandó kulcs bekérése a felhasználótól
    key = input("Kérem írja be a kulcsot a titkosításhoz! \n")
    print("A titkos kulcs:", key)

    # A könnyebb kezelés érdekében a kulcsot és a titkosítandó szót is kisbetükre konvertáljuk
    plaintext = plaintext.lower()
    key = key.lower()

    # Majd eltávolítjuk az összes space-t
    plaintext = RemoveSpaces(plaintext)
    key = RemoveSpaces(key)

    # Kiegészítjük a szót
    plaintext = Prepare(plaintext)

    # Legeneráljuk a kulcs táblát, ami 2d-s tömb
    keyTableArray = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    keyTableArray = GenerateKeyTable(key, keyTableArray)

    return Encrypt(plaintext, keyTableArray)

result = EncryptWithPlayfair()
print("A titkosított változat", result)
