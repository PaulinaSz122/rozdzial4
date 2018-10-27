inventory = ("miecz", "zroja", "tarcza", "napój uzdrawiający")
print("Elementy Twojego inwentarza:")
for item in inventory:
    print(item)

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

print("Twój dobytek zawiera", len(inventory), "elementy(-ów).")

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

start = int(input("\nWprowadź indeks wyznaczający początek wycinka: "))
finish = int(input("\nWprowadź indeks wyznaczający koniec wycinka: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

chest = ("złoto", "klejnoty")
print("Znajdujesz skrzynię, która zawiera:")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
