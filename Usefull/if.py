def hoopCount(n):
    return "Keep at it until you get it" if n<10 else "Great, now move on to tricks"

print(hoopCount(10))

def get_real_floor(n):
    return n - 2 if n > 13 else n - 1 if n > 0 else n