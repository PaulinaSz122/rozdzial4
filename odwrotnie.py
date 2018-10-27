komunikat = input("Podaj komunikat: ")

odwrotny = ""

for i in range(len(komunikat) - 1, -1, -1):
    odwrotny += komunikat[i]

print("\nOto komunikat w odwrotnej kolejności:")
print(odwrotny)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
