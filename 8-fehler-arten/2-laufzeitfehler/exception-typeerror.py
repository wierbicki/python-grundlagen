try:
    print("4" + 2)   # String und Integer kombiniert (TypeError)
except Exception as e:
    print(type(e).__name__)