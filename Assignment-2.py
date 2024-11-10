digits = '0123456789ABCDEF'

def decimal_to_binary(number, system=2):
    final = ''
    while number > 0:
        final = digits[number % system] + final
        number //= system
    return final

def binary_to_decimal(number, system=2):
    final = 0
    for i, digit in enumerate(number[::-1]):
        final += digits.index(digit) * (system ** i)
    return final

def sixteen_to_decimal(number, system=16):
    final = 0
    for i, digit in enumerate(number[::-1]):
        final += digits.index(digit) * (system ** i)
    return final

def main():
    number = input("Enter a number (level 1 : if decimal - without prefix, if binary - with prefix 0b, level 2 : if hexadecimal - with prefix 0x) : ")
    while not (number[0:2] == "0b" or number.isdecimal() or number[0:2] == "0x"):
        number = input("Enter a number (level 1 : if decimal - without prefix, if binary - with prefix 0b, level 2 : if hexadecimal - with prefix 0x) : ")
    if number[0:2] == '0b':
        print(f"Your number {number} in decimal - {binary_to_decimal(number[2:])}")
    elif number[0:2] == '0x':
        decimal_from_16 = sixteen_to_decimal(number[2:])
        what_system = input("What system do you want to convert to? (decimal - d, binary - b) : ")
        while not (what_system == 'd' or what_system == 'b'):
            what_system = input("What system do you want to convert to? (decimal - d, binary - b) : ")
        if what_system == 'd':
            print(f"Your number {number} in hexadecimal number system - {decimal_from_16}")
        else:
            print(f"Your number {number} in hexadecimal number system - {decimal_to_binary(decimal_from_16)}")
    else:
        print(f"Your number {number} in binary - {decimal_to_binary(int(number))}")
    again = input("Do you want to repeat? y/n : ")
    if again == 'y':
        main()
    else:
        print("Ok! Seeyuh")

main()