# KalkulatorTrueProportion-Wyborczy
Kalkulator w Pythonie pokazujący True proportion czyli liczbę mandatów proporcjonalnie do otrzymanych głosów

## Wyniki dla przykładu pochodzą z okręgu 5 do Sejmu Rzeczypospolitej Polskiej

pis =   182648
ko =    119526
sld =    67076
psl =    49225
kwin =   28525

## Wyniki na komitety które przekroczyły próg (5%)

Na ich podstawie tworzymy sumę głosów oddanych

glosy_oddane = pis + ko + sld + psl + kwin

## Potrzebna jest nam również liczba mandatów możliwych do uzyskania w danym okręgu 

suma_mandatow = 13

## Obliczenie jest stosunkowo proste ilość głosów oddanych mnożymy przez sumę mandatów w danym okręgu i wynik dzielimi przez sumę wszystkich głosów

pis_mandaty = (pis * suma_mandatow / glosy_oddane)
...

## Później, aby wynik był bardziej czytelny zapisujemy go tak

print("PiS mandaty: ", round(pis_mandaty, 2))
...


round() zaokrągli nam wynik do 2 miejsc po przecinku