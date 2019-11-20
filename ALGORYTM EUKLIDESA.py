print("Algorytm Euklidesa")

a = int(input("Wpisz pierwszą liczbę: "))
b = int(input("Wpisz drugą liczbę: "))

while a != b:
    if a > b:
        a = a - b
    if a < b:
        b = b - a
    if a == b:
        print("Największy wspólny dzielnik wynosi: ", a)