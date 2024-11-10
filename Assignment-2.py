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

def main():
    number = input("Enter a number (if decimal - without prefix, if binary - with prefix 0b) : ")
    while not (number[0:2] == "0b" or number.isdecimal()):
        number = input("Enter a number (if decimal - without prefix, if binary - with prefix 0b) : ")
    if number[0:2] == '0b':
        decimal_from_binary = binary_to_decimal(number[2:])
        print(f"Your number {number} in decimal - {binary_to_decimal(number[2:])}")
    else:
        print(f"Your number {number} in binary - {decimal_to_binary(int(number))}")
    again = input("Do you want to repeat? y/n : ")
    if again == 'y':
        main()
    else:
        print("Ok! Seeyuh")
main()