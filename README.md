# Playfair titkosítás python-ban

Wikipédia a Playfair titkosításról: [Wikipédia](https://en.wikipedia.org/wiki/Playfair_cipher)

## Készítette: Sipos Attila

Használt python verzió: 3.8.10

A projekthez használt források:
- [https://medium.com/analytics-vidhya/play-fair-cipher-encryption-using-python3-f91c42931f52](https://medium.com/analytics-vidhya/play-fair-cipher-encryption-using-python3-f91c42931f52)
- [https://www.geeksforgeeks.org/playfair-cipher-with-examples/](https://www.geeksforgeeks.org/playfair-cipher-with-examples/)

A Playfair titkosítást, ami egy manuális szimetrikus titkosítás [Charles Wheatstone](https://en.wikipedia.org/wiki/Charles_Wheatstone) 1854 találta ki. A Playfair titkosítást nehezebb feltörni mivel ellenáll a tendenciaelőfordulás támadásoknak. Leheteséges azonban feltörni más pár tendenciaelőfordulás támadással viszont eléggé nehéz. Mivel 600 darab pár fordulhat, amit az angol ábécé segítségévél hoznak létre, ami 26 betüből áll. Azt viszont tudni kell, hogy csak 25-öt használunk mivel a "j" és a "i" között nem teszünk különbséget. A jelenlegi implementációban az "i" karaktert használjuk.

Ez a projekt titkosításra és dekódolásra is alkalmas!!!

## Mi a folyamat?

A folyamat három lépésből áll:
- A megadott titkosítandó szöveget betüpárokba rendezzük ennek viszont van egy megkötése:
    - Kettő egyforma betü nem szerepelhet egymás mellett így a szöveget kiegészítjük egy extra betüvel, ami ritkábban fordul elő az angol szavakban jelen esetben ez az "x"
    - Ha a szöveg hossza páratlan tehát az utolsó párból egy betü hiányzik akkor ki kell egészíteni jelen esetben ez az "x" karakterrel történik
- Generálni kell egy kulcs táblát ez egy 5x5-ös kétdimenziós mátrix, amibe a kulcsot és az angol ábécé betüit helyezzük el ábécé sorrendben
- Titkosítani kell a megadott szöveget, amit a kulcs tábla segítségével és három egyszerű szabállyal teszünk meg:
    - Ha a betüpárban szereplő karakterek mátrixban elfoglalt helyének a sora egyezik akkor azokat eltojuk jobbra egyel
    - Ha a betüpárban szereplő karakterek mátrixban elfoglalt helyének a oszlopa egyezik akkor azokat eltoljuk lefelé egyel
    - Ha a betüpárban szereplő karakterek mátrixban elfoglalt helyének sem a sora, sem az oszlopa nem egyezik meg akkor a sor koordináta változatlan marad de az oszlop koordináta megcserélődik

## Hogyan kell futtatni?

linux alatt: ./playfair.py

windows alatt: python playfair.py
