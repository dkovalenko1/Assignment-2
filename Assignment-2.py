from unicodedata import digit, numeric

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

def decimal_to_any(number, system):
    final = ''
    while number > 0:
        final = digits[number % system] + final
        number //= system
    return final

def any_to_decimal(number, system):
    final = 0
    for i, digit in enumerate(number[::-1]):
        final += digits.index(digit) * (system ** i)
    return final

def main():
    level = input('Enter a level : ')
    while not level in ['1', '2', '3']:
        level = input('Enter correct level(1-3) : ')
    if level == '1' or level == '2':
        number = input("Enter a number (level 1 : if decimal - without prefix, if binary - with prefix 0b, level 2 : if hexadecimal - with prefix 0x : ")
        while not (number[0:2] == "0b" or number.isdecimal() or number[0:2] == "0x" or number[-2] == 'x' or number[-3] == 'x'):
            number = input("Enter a number (level 1 : if decimal - without prefix, if binary - with prefix 0b, level 2 : if hexadecimal - with prefix 0x : ")
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

    if level == '3':
        number = input("Enter a number (level 3) : ")
        if int(number[-1:]) >16:
            print("Error! We only support systems up to 16. Try again.")
            main()
        if number[-2] == 'x' or number[-2] == 'X':
            number_from_digits = digits[:int(number[-1])]
            num_list = list(number[:-2])
            for i in num_list:
                if i not in number_from_digits:
                    print("Error!(system and number do not match) Try again")
                    main()
            to_decimal = any_to_decimal(number[:-2], int(number[-1]))
            what_system = int(input(f"To what system do u want to convert number {number[:-2]}? : "))
            if not what_system in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
                print("Error! We only support systems up to 16. Try again.")
                main()
            print(decimal_to_any(to_decimal, what_system))

        elif number[-3] == 'x' or number[-3] == 'X':
            if int(number[-2:]) > 16:
                print("Error! We only support systems up to 16. Try again.")
                main()
            number_from_digits = digits[:int(number[-2:])]
            num_list = list(number[:-3])
            for i in num_list:
                if i not in number_from_digits:
                    print("Error! Try again")
                    main()
            to_decimal = any_to_decimal(number[:-3], int(number[-2:]))
            what_system = int(input(f"To what system do u want to convert number {number[:-3]}? : "))
            if not what_system in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
                print("Error! We only support systems up to 16. Try again.")
                main()
            print(f"Result : {decimal_to_any(to_decimal, what_system)}")
        else:
            print("Error!(no x) Try again")
            main()

    again = input("Do you want to repeat? y/n : ")
    if again == 'y':
        main()
    else:
        print("Ok! Seeyuh")

main()