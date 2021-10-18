#! /usr/bin/env python3

# A dokumentáció a README.md-ben található
# Ezen a linken jobban olvasható formátumban is megtalálható: https://github.com/Siposattila/playfair-encryption

# Ez a funkció behelyettesíti a szóközöket
def SpaceConversion(string):
    convertedString = ""
    for i in string:
        if i == " ":
            convertedString += '_'
        elif i == "_":
            convertedString += ' '
        else: convertedString += i
    return convertedString

# A funckció lényege, hogy megfogjon egy karaktert és beillesze a szövegbe tetszőleges helyre
def InsertChar(string, charToInsert, position):
    return string[:position] + charToInsert + string[position:]

# Ebben a funkcióban a szót, amit megadnak feldaraboljuk és ha kettő
# ugyanolyan karakter szerepel egymás mellett akkor beillesztünk egy extra karaktert, ami jelenesetben az x
def Prepare(string):
    plaintextArray = []
    
    # string = SpaceConversion(string)
    if len(string) % 2 != 0:
        string += 'x'

    i = 0
    while i < len(string):
        if i + 2 > len(string):
            break
        if string[i] == string[i + 1]:
            plaintextArray.append([string[i], 'x'])
            string = InsertChar(string, 'x', i+1)
        else:
            plaintextArray.append([string[i], string[i + 1]])
        i += 2

    return plaintextArray

# Ez a funkció felelős a kulcs feldolgozásáért és a kulcstábla létrehozásáért, ami egy 6*6-os mátrix
def GenerateKeyTable(key, keyTableArray):
    alphabet = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ö', 'ő', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'ű', 'v', 'w', 'x', 'y', 'z', '_']
    keyArray = [] 

    # key = SpaceConversion(key)
    for i in range(len(key)):
        if key[i] not in keyArray:
            keyArray.append(key[i])
    
    for i in range(len(alphabet)):
        if alphabet[i] not in keyArray:
            keyArray.append(alphabet[i])

    k = 0
    for i in range(len(keyTableArray)):
        for j in range(len(keyTableArray)):
            keyTableArray[i][j] = keyArray[k]
            k += 1

    return keyTableArray

# Ez a funkció visszaadja az adott karakterek pozicióját
def Search(keyTableArray, char):
    position = []

    for i in range(len(keyTableArray)):
        for j in range(len(keyTableArray)):
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
            if positionA[1] + 1 > 5:
                positionA[1] = 0
            else:
                positionA[1] += 1
            if positionB[1] + 1 > 5:
                positionB[1] = 0
            else:
                positionB[1] += 1

            encryptedCiphertext += keyTableArray[positionA[0]][positionA[1]]
            encryptedCiphertext += keyTableArray[positionB[0]][positionB[1]]
        elif positionA[1] == positionB[1]:
            if positionA[0] + 1 > 5:
                positionA[0] = 0
            else:
                positionA[0] += 1
            if positionB[0] + 1 > 5:
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
            if positionA[1] - 1 > 5:
                positionA[1] = 0
            else:
                positionA[1] -= 1
            if positionB[1] - 1 > 5:
                positionB[1] = 0
            else:
                positionB[1] -= 1

            decryptedCiphertext += keyTableArray[positionA[0]][positionA[1]]
            decryptedCiphertext += keyTableArray[positionB[0]][positionB[1]]
        elif positionA[1] == positionB[1]:
            if positionA[0] - 1 > 5:
                positionA[0] = 0
            else:
                positionA[0] -= 1
            if positionB[0] - 1 > 5:
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
    plaintext = "Szia haver hogyan vagy merre voltál"
    plaintext = plaintext.lower()
    plaintext = plaintext.strip()
    print("A titkosítani kívánt szó:", plaintext)
    plaintext = SpaceConversion(plaintext)

    # A könnyebb kezelés érdekében a kulcsot és a titkosítandó szót is kisbetűkre konvertáljuk
    key = "haver"
    key = key.lower()
    key = key.strip()
    print("A titkos kulcs:", key)
    key = SpaceConversion(key)

    # Kiegészítjük a szót és feldaraboljuk párokra
    plaintext = Prepare(plaintext)

    # Legeneráljuk a kulcs táblát, ami egy két dimenziós mátrix
    keyTableArray = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    keyTableArray = GenerateKeyTable(key, keyTableArray)

    return Encrypt(plaintext, keyTableArray)

# A mindent elvégző funkció
def DecryptWithPlayfair():
    # Titkosított szó bekérése a felhasználótól
    # A könnyebb kezelés érdekében a kulcsot és a titkosított szót is kisbetűkre konvertáljuk
    ciphertext = input("Kérem írja be a titkosított szót! \n")
    ciphertext = ciphertext.lower()
    ciphertext = ciphertext.strip()
    print("A titkosított szó:", ciphertext, "\n")

    # A könnyebb kezelés érdekében a kulcsot és a titkosított szót is kisbetűkre konvertáljuk
    key = "haver"
    key = key.lower()
    key = key.strip()
    print("A titkos kulcs:", key)
    key = SpaceConversion(key)

    # Feldaraboljuk párokra a titkosított szót a dekódoláshoz
    ciphertext = Prepare(ciphertext)

    # Legeneráljuk a kulcs táblát, ami egy két dimenziós mátrix
    keyTableArray = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    keyTableArray = GenerateKeyTable(key, keyTableArray)

    return SpaceConversion(Decrypt(ciphertext, keyTableArray))

encryptResult = EncryptWithPlayfair()
print("A titkosított változat: ", encryptResult, "\n")

decryptResult = DecryptWithPlayfair()
print("Az eredeti olvasható változat: ", decryptResult)
