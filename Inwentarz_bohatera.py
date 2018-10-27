inventory = ()

if not inventory:
    print("Nie posiadasz niczego.")

input("\nAby kontynuować misję, naciśnij Enter")

inventory = ("miecz", "zbroja", "tarcza", "napój uzdrawiający")

print("\nWykaz zawartości krotki:")
print(inventory)

print("Elementy twojego wyposażenia:")
for item in inventory:
    print(item)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
