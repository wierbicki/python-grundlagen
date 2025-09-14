try:
    print(zahl)   # Variable nicht definiert (NameError)
except Exception as e:
    print(type(e).__name__)