STICKS_PER_DOOS = 5

aantal_sticks = int(input("Hoeveel USB-sticks heb je nodig? "))

aantal_volledige_dozen = aantal_sticks // STICKS_PER_DOOS
aantal_losse_sticks = aantal_sticks % STICKS_PER_DOOS

totaal_aantal_dozen = aantal_volledige_dozen
if aantal_losse_sticks > 0:
    totaal_aantal_dozen += 1

print("---", "Bestelling", "---", sep=" ")
print(f"Aantal volledige dozen: {aantal_volledige_dozen}\n"
      f"Aantal overblijvende losse sticks: {aantal_losse_sticks}")
print(f"De bestelling bestaat uit {totaal_aantal_dozen} dozen.")
