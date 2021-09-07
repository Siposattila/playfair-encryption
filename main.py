#! /usr/bin/env python3
import numpy as np

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

stringArray = np.array()
keyArray = np.array()

# Ez a funckció eltávolítja az összes lehetséges space-t
def RemoveSpaces(string):
    for i in string:
        if i == ' ':
            i = ''
    return string

# Ha a szó hossza nem egyenletes vagyis nem osztója a 2 akkor hozzáadunk egy extra karaktert ebben az esetben a z lesz az
def Prepare(string):
    if len(string) % 2 != 0:
        string[len(string)] = 'z'
    return string

# Ezzel a funkcióval készítjük el az 5x5-ös két dimenziós kulcs táblánkat
def GenerateKeyTable(key, keyTable):
    dicty = dict()

    for i in key:
        if i != 'j':
            dicty[i - 97] = 2
    
    dicty['j' - 97] = 1

    j = 0
    i = 0

    for k in key:
        if dicty[k - 97] == 2:
            dicty[k - 97] -= 1
            keyTable[i][j] = key[k]
            j++
            if j == 5:
                i++
                j = 0
    
    for k in 26:
        if dicty[k] == 0:
            keyTable[i][j] = chr(k + 97)
            j++
            if j == 5:
                i++
                j = 0
