# this will try to use the collatz squar
# if number even return number // 2, sinon number * 3 +1


def collatz(number):
    if number % 2 == 0:
        b = number // 2
        print(b)
    else:
        b = number * 3 + 1
        print(b)


b = (int(input("Taper un chiffre: ")))
while b != 1:
    collatz(b)
