cryptogram = ("VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR")

common_words = set([
    "the", "and", "is", "in", "to", "a", "of", "that", "it", "with",
    "for", "on", "was", "at", "by", "as", "but", "be", "or", "this",
    "which", "from", "an", "are", "not", "we", "they", "you", "will",
    "can", "has", "have", "or", "if", "what", "there", "where", "who",
    "when", "how", "more", "so", "my", "all", "one", "has", "had", "up",
    "do", "your", "him", "her", "his", "she", "he", "there", "were", "will"
])

best_score = 0
best_shift = None
best_decryption = ""

for shift in range(1, 26):
    decrypted_text = ''
    for char in cryptogram:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char
    
    words = set(decrypted_text.lower().split())
    score = sum(1 for word in words if word in common_words)
    
    if score > best_score:
        best_score = score
        best_shift = shift
        best_decryption = decrypted_text

print(f"Shift Key Value: {best_shift}")
print(f"Decrypted text: {best_decryption}")
