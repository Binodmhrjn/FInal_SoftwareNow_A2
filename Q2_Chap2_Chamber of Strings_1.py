s = input("Enter a string of at least 16 characters (with both numbers and letters): ")

if len(s) < 16:
    print("The string is too short. It must be at least 16 characters long.")
else:
    numbers = ""
    letters = ""

    for char in s:
        if char.isdigit():
            numbers += char
        elif char.isalpha():
            letters += char

    print("Numbers substring:", numbers)
    print("Letters substring:", letters)

    even_numbers = ""
    for char in numbers:
        if int(char) % 2 == 0:
            even_numbers += char
    print("Even numbers:", even_numbers)

    uppercase_letters = ""
    for char in letters:
        if char.isupper():
            uppercase_letters += char
    print("Uppercase letters:", uppercase_letters)

    print("ASCII values of even numbers:", [ord(char) for char in even_numbers])

    print("ASCII values of uppercase letters:", [ord(char) for char in uppercase_letters])
