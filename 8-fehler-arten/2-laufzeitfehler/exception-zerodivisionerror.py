try:
    print(1 / 0)   # Division durch 0 (ZeroDivisionError)
except Exception as e:
    print(type(e).__name__)