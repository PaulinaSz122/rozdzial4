licz_pocz = int(input("Podaj liczbę początkową: "))
licz_kon = int(input("Podaj liczbę końcową: "))
krok = int(input("Podaj wielkość odstępu: "))

print()

for i in range(licz_pocz, licz_kon, krok):
    print(i)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
