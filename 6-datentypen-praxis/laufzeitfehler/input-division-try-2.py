try:
   zahl1 = float(input("Zahl 1: "))
   zahl2 = float(input("Zahl 2: "))
   print(zahl1 / zahl2) 
except Exception as e:
   print(f"Fehler: {e}")

input("Taste drücken...")
