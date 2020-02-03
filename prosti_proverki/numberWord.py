def singleDigit(number):
    if number == 0:
        word = "zero"
    elif number == 1:
        word = "one"
    elif number == 2:
        word = "two"
    elif number == 3:
        word = "three"
    elif number == 4:
        word = "four"
    elif number == 5:
        word = "five"
    elif number == 6:
        word = "six"
    elif number == 7:
        word = "seven"
    elif number == 8:
        word = "eigth"
    elif number == 9:
        word = "nine"
    elif number == 10:
        word = "ten"
    return word

def doubleDigit(firstDigit,secondDigit):
    if firstDigit == 2 and secondDigit == 0:
        print("twenty")
    elif firstDigit == 2:
        firstDigitWord = "twenty"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")
    if firstDigit == 3 and secondDigit == 0:
        print("thirty")
    elif firstDigit == 3:
        firstDigitWord = "thirty"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")
    if firstDigit == 4 and secondDigit == 0:
        print("forty")
    elif firstDigit == 4:
        firstDigitWord = "forty"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")
    if firstDigit == 5 and secondDigit == 0:
        print("fifty")
    elif firstDigit == 5:
        firstDigitWord = "fifty"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")
    if firstDigit == 6 and secondDigit == 0:
        print("sixty")
    elif firstDigit == 6:
        firstDigitWord = "sixty"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")
    if firstDigit == 7 and secondDigit == 0:
        print("seventy")
    elif firstDigit == 7:
        firstDigitWord = "seventy"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")
    if firstDigit == 8 and secondDigit == 0:
        print("eighty")
    elif firstDigit == 8:
        firstDigitWord = "eighty"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")
    if firstDigit == 9 and secondDigit == 0:
        print("ninety")
    elif firstDigit == 9:
        firstDigitWord = "ninety"
        secondDigitWord = singleDigit(secondDigit)
        print(f"{firstDigitWord} {secondDigitWord}")

digits = int(input())
if digits <= 10:
    print(singleDigit(digits))
elif digits < 100:
    firstDigit = digits / 10
    firstDigit = int(firstDigit)
    secondDigit = digits % 10
    doubleDigit(firstDigit,secondDigit)
elif digits == 100:
    print("one hundred")