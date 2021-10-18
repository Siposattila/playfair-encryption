#! /usr/bin/env python3

# A dokumentáció a README.md-ben található
# Ezen a linken jobban olvasható formátumban is megtalálható: https://github.com/Siposattila/playfair-encryption

# Ez a funckció eltávolítja az összes lehetséges space-t
def RemoveSpaces(string):
    cleanedString = ""
    for i in string:
        if i != " ":
            cleanedString += i
    return cleanedString

# A funckció lényege, hogy megfogjon egy karaktert és beillesze a szövegbe tetszőleges helyre
def InsertChar(string, charToInsert, position):
    return string[:position] + charToInsert + string[position:]

# Ebben a funkcióban a szót, amit megadnak feldaraboljuk és ha kettő
# ugyanolyan karakter szerepel egymás mellett akkor beillesztünk egy extra karaktert, ami jelenesetben az x
def Prepare(string):
    plaintextArray = []
    length = len(string)

    i = 0
    while i < length:
        if string[i] == string[i + 1]:
            plaintextArray.append([string[i], 'x'])
            string = InsertChar(string, 'x', i+1)
            length += 1
        else:
            plaintextArray.append([string[i], string[i + 1]])
        i += 2

    return plaintextArray

# Ez a funkció felelős a kulcs feldolgozásáért és a kulcstábla létrehozásáért, ami egy 5*5-ös mátrix
def GenerateKeyTable(key, keyTableArray):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    keyArray = []
    length = len(key)

    for i in range(length):
        if key[i] not in keyArray:
            if key[i] == 'j':
                i += 1
            else:
                keyArray.append(key[i])
    
    for i in range(len(alphabet)):
        if alphabet[i] not in keyArray:
            if alphabet[i] == 'j':
                i += 1
            else:
                keyArray.append(alphabet[i])

    k = 0
    for i in range(5):
        for j in range(5):
            keyTableArray[i][j] = keyArray[k]
            k += 1

    return keyTableArray

# Ez a funkció visszaadja az adott karakterek pozicióját
def Search(keyTableArray, char):
    position = []

    for i in range(5):
        for j in range(5):
            if keyTableArray[i][j] == char:
                position.append(i)
                position.append(j)

    return position

# Ezzel a funkcióval végezzük el a titkosítást
def Encrypt(plaintextArray, keyTableArray):
    encryptedCiphertext = ""

    for i in range(len(plaintextArray)):
        positionA = Search(keyTableArray, plaintextArray[i][0])
        positionB = Search(keyTableArray, plaintextArray[i][1])

        if positionA[0] == positionB[0]:
            if positionA[1] + 1 > 4:
                positionA[1] = 0
            else:
                positionA[1] += 1
            if positionB[1] + 1 > 4:
                positionB[1] = 0
            else:
                positionB[1] += 1

            encryptedCiphertext += keyTableArray[positionA[0]][positionA[1]]
            encryptedCiphertext += keyTableArray[positionB[0]][positionB[1]]
        elif positionA[1] == positionB[1]:
            if positionA[0] + 1 > 4:
                positionA[0] = 0
            else:
                positionA[0] += 1
            if positionB[0] + 1 > 4:
                positionB[0] = 0
            else:
                positionB[0] += 1

            encryptedCiphertext += keyTableArray[positionA[0]][positionA[1]]
            encryptedCiphertext += keyTableArray[positionB[0]][positionB[1]]
        else:
            encryptedCiphertext += keyTableArray[positionA[0]][positionB[1]]
            encryptedCiphertext += keyTableArray[positionB[0]][positionA[1]]

    return encryptedCiphertext

# Ezzel a funkcióval végezzük el a dekódolást
def Decrypt(ciphertextArray, keyTableArray):
    decryptedCiphertext = ""

    for i in range(len(ciphertextArray)):
        positionA = Search(keyTableArray, ciphertextArray[i][0])
        positionB = Search(keyTableArray, ciphertextArray[i][1])

        if positionA[0] == positionB[0]:
            if positionA[1] - 1 > 4:
                positionA[1] = 0
            else:
                positionA[1] -= 1
            if positionB[1] - 1 > 4:
                positionB[1] = 0
            else:
                positionB[1] -= 1

            decryptedCiphertext += keyTableArray[positionA[0]][positionA[1]]
            decryptedCiphertext += keyTableArray[positionB[0]][positionB[1]]
        elif positionA[1] == positionB[1]:
            if positionA[0] - 1 > 4:
                positionA[0] = 0
            else:
                positionA[0] -= 1
            if positionB[0] - 1 > 4:
                positionB[0] = 0
            else:
                positionB[0] -= 1

            decryptedCiphertext += keyTableArray[positionA[0]][positionA[1]]
            decryptedCiphertext += keyTableArray[positionB[0]][positionB[1]]
        else:
            decryptedCiphertext += keyTableArray[positionA[0]][positionB[1]]
            decryptedCiphertext += keyTableArray[positionB[0]][positionA[1]]

    return decryptedCiphertext

# A mindent elvégző funkció
def EncryptWithPlayfair():
    # A könnyebb kezelés érdekében a kulcsot és a titkosítandó szót is kisbetűkre konvertáljuk
    # Majd eltávolítjuk az összes space-t
    plaintext = "helLo tHere My friEnd thIs iS a sEcret"
    plaintext = plaintext.lower()
    plaintext = RemoveSpaces(plaintext)
    print("A titkosítani kívánt szó:", plaintext)

    # A könnyebb kezelés érdekében a kulcsot és a titkosítandó szót is kisbetűkre konvertáljuk
    # Majd eltávolítjuk az összes space-t
    key = "frIenDs alWaYs BetRay"
    key = key.lower()
    key = RemoveSpaces(key)
    print("A titkos kulcs:", key)

    # Kiegészítjük a szót és feldaraboljuk párokra
    plaintext = Prepare(plaintext)

    # Legeneráljuk a kulcs táblát, ami egy két dimenziós mátrix
    keyTableArray = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    keyTableArray = GenerateKeyTable(key, keyTableArray)

    return Encrypt(plaintext, keyTableArray)

# A mindent elvégző funkció
def DecryptWithPlayfair():
    # Titkosított szó bekérése a felhasználótól
    # A könnyebb kezelés érdekében a kulcsot és a titkosított szót is kisbetűkre konvertáljuk
    # Majd eltávolítjuk az összes space-t
    ciphertext = input("Kérem írja be a titkosított szót! \n")
    ciphertext = ciphertext.lower()
    ciphertext = RemoveSpaces(ciphertext)
    print("A titkosított szó:", ciphertext, "\n")

    # A könnyebb kezelés érdekében a kulcsot és a titkosított szót is kisbetűkre konvertáljuk
    # Majd eltávolítjuk az összes space-t
    key = "frIenDs alWaYs BetRay"
    key = key.lower()
    key = RemoveSpaces(key)
    print("A titkos kulcs:", key)

    # Feldaraboljuk párokra a titkosított szót a dekódoláshoz
    ciphertext = Prepare(ciphertext)

    # Legeneráljuk a kulcs táblát, ami egy két dimenziós mátrix
    keyTableArray = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    keyTableArray = GenerateKeyTable(key, keyTableArray)

    return Decrypt(ciphertext, keyTableArray)

encryptResult = EncryptWithPlayfair()
print("A titkosított változat", encryptResult, "\n")

decryptResult = DecryptWithPlayfair()
print("Az eredeti olvasható változat", decryptResult)
