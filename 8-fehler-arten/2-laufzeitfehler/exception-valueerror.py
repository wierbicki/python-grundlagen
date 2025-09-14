try:
    zahl = int("Vier")   # String in Integer (ValueError)
except Exception as e:
    print(type(e).__name__)