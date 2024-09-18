def decrypt(text, key):
    decrypted_text = ""

    # Iterate through every character
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key  # Shifts character back by the key
            # Checks for an uppercase letter
            if char.isupper():
                if shifted < ord("A"):
                    shifted += 26
                elif shifted > ord("Z"):
                    shifted -= 26
                # shifts uppercase alphabet

            # Checks for a lowercase letter
            elif char.islower():
                if shifted < ord("a"):
                    shifted += 26
                elif shifted > ord("z"):
                    shifted -= 26
                # shifts lowercase alphabet

            decrypted_text += chr(shifted)  # Add shifted character to result
        else:
            decrypted_text += (
                char  # If it's not a letter, the character remains the same
            )

    return decrypted_text


# Provided encrypted code
encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbaner!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# Retreived the key from the given code i.e. 13
shift_val = 13
decrypted_code = decrypt(encrypted_code, shift_val)

print("Decrypted Code:")
print(decrypted_code)
