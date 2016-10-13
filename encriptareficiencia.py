import string

def shiftedDict(shift):
    lowercase_letters = string.ascii_lowercase
    shifted_dictionary = {}
    for letter in range(len(lowercase_letters)):
        if letter + shift < 26:
            shifted_dictionary[lowercase_letters[letter]] = lowercase_letters[letter + shift]
        else:
            shifted_dictionary[lowercase_letters[letter]] = lowercase_letters[(letter + shift)-26]
    return shifted_dictionary

def encryptMessage(message, shift):
    shifted_dick = shiftedDict(shift)  # Our dick-tionary
    encrypted_text = ""
    for letter in message:
        if letter in string.ascii_lowercase:
            encrypted_text += shifted_dick[letter]
        else:
            encrypted_text += letter
    return encrypted_text

def uncypherMessage(encrypted, shift):
    shifted_dick = shiftedDict(26-shift)  # Our dick-tionary
    plain_text = ""
    for letter in encrypted:
        if letter in string.ascii_lowercase:
            plain_text += shifted_dick[letter]
        else:
            plain_text += letter
    return plain_text


text = input("Dame un texto por favor")
texto_encriptado = encryptMessage(text, 10)
print(texto_encriptado)
plain_text = uncypherMessage(texto_encriptado, 10)
print(plain_text)
