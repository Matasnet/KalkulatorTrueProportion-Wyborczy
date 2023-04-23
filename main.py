# zapisujesz ile głosów otrzymała dana partia
pis =   182648
ko =    119526
sld =    67076
psl =    49225
kwin =   28525

# suma mandatów na dany okręg
suma_mandatow = 13

# suma głosów oddanych w okręgu
glosy_oddane = pis + ko + sld + psl + kwin

# wyliczenie współczynnika nazwa_partii * suma_mandatów / głosy_oddane
pis_mandaty = (pis * suma_mandatow / glosy_oddane)
ko_mandaty = (ko * suma_mandatow / glosy_oddane)
sld_mandaty = (sld * suma_mandatow / glosy_oddane)
psl_mandaty = (psl * suma_mandatow / glosy_oddane)
kwin_mandaty = (kwin * suma_mandatow / glosy_oddane)

# wypisanie wyników zaokrąglonych do 2 miejsca po przecinku
print("PiS mandaty: ", round(pis_mandaty, 2))
print("KO mandaty: ", round(ko_mandaty, 2))
print("SLD mandaty: ", round(sld_mandaty, 2))
print("PSL mandaty: ", round(psl_mandaty, 2))
print("KWIN mandaty: ", round(kwin_mandaty, 2))

'''
Jest to iloraz wyborczy przy domyślnych wartościach oznacza on, że na 13 osób wchodzących do komisji wyborczej:
5,3 głosowało na PiS 
3,4 na KO 
1,9 na SLD 
1,4 na PSL 
0,8 na KWiN 
___ 
~13 
Można to interpretować tak, że na 13 osób wchodzących szansa na oddanie głosu na KWiN była mniejsza niż na 2 wyborców SLD

Należy pamiętać, że nie jest to ilość mandatów bezpośrednich a tylko mandaty proporcjonalne do otrzymanych głosów.
'''