active = True


def encode(num):
    length = len(str((num)))
    enc = ''
    num = list(str(num))
    for i in range(length):
        num[i] = int(num[i]) + 3
        enc += str(num[i])
    return enc


def decode(num):
    length = len(str((num)))
    enc = ''
    num = list(str(num))
    for i in range(length):
        num[i] = int(num[i]) - 3
        enc += str(num[i])
    return enc


store = 0
while active:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        store = encode(password)
        print("Your password has been encoded and stored!")
    if option == 2:
        dec = decode(store)
        print(f"The encoded password is " + store + ", and the original password is " + dec)
    if option == 3:
        break