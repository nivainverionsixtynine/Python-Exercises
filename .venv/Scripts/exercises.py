

def addValues():
    numberA = int(input("Add number 01: "))
    numberB = int(input("Add number 02: "))

    print(f"Sum: {numberA + numberB}")


def leapyear():
    year = int(input("what year: "))
    if year %4 == 0:
        print("leap year")
    else :
        print("not leap year")
leapyear()


