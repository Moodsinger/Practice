def DigitCounter(x):
    if x < 10: return 1
    else:
        return DigitCounter(x/10) + 1

print(DigitCounter(111111111111111111))
