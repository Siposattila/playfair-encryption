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

def Prepare(string):
    if len(string) % 2 != 0:
        string[len(string)] = 'z'
    return string


