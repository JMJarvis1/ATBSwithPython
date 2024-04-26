"""Affine Cipher, by Al Sweigart al@inventwithpython.com
The affine cipher is a simple substitution cipher that uses addition and
multiplication to encrypt and decrypt symbols.
More info at: https://en.wikipedia.org/wiki/Affine_cipher
This and other games are available at https://nostarch.com/XX
Tags: large, cryptography, math, pyperclip"""

__version__ = 0

try:
    import pyperclip  # pyperclip copies text to the clipboard
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

import random
from re import S

# Note the space at the front of the SYMBOLS string:
SYMBOLS = (
    """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEF"""
    + """GHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
)


def main():
    print("""Affine Cipher, by Al Sweigart al@inventwithpython.com
The affine ciper is a simple substitution cipher that uses addition and 
multiplication to encrypt and decrypt symbols.""")

    # Let the user specify if they are encrypting or decrypting:
    while True:  # Keep asking until the user enters an 'e' or a 'd'.
        response = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ").lower()
        if response.startswith("e"):
            myMode = "encrypt"
            break
        elif response.startswith("d"):
            myMode = "decrypt"
            break
        print("Please enter the letter 'e' or 'd'.")

    # Let the user specify the key to use:
    while True:  # Keep asking until the user enters a valid key.
        keyRequestMessage = (
            "Please specify the key that you wish to use,"
            + "or RANDOM to have one generated for you:\n> "
        )
        response = input(keyRequestMessage).upper()
        if response == "RANDOM":
            myKey = generateRandomKey()
            print(f"The key is {myKey}. KEEP THIS SECRET!")
            break
        else:
            if not response.isdecimal():
                print("This key is not a number.")
                continue
            if checkKey(int(response), myMode):
                myKey = int(response)
                break

    # Let the user specify the message to encrypt/decrypt:
    myMessage = input(f"Enter the message to {myMode}:\n> ")

    if myMode == "encrypt":
        translated = encryptMessage(myKey, myMessage)
    elif myMode == "decrypt":
        translated = decryptMessage(myKey, myMessage)
    print(f"{myMode}ed text:\n{translated}")

    try:
        pyperclip.copy(translated)
        print(f"Full {mymode}ed text copied to clipboard.")
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def getKeyPartsFromKey(key):
    """Get the two key A and key B parts from the key."""
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKey(key, mode):
    """Return True if key is a valid encryption key for this mode.
    Otherwise return False."""
    keyA, keyB = getKeyPartsFromKey(key)
    if mode == "encrypt" and keyA == 1 and keyB == 0:
        print(
            "This key effectively doesn not do any encryption on the"
            + "message. Choose a different key."
        )
        return False
    elif keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        print(
            "Key A must be greater than 0 and Key B must be between"
            + f"0 and {(SYMBOLS) - 1}"
        )
        return False
    elif gcd(keyA, len(SYMBOLS)) != 1:
        print(
            f"Key A ({keyA}) and the symbols set"
            + f"size ({len(SYMBOLS)}) are not relatively prime."
            + "Choose a different key."
        )
        return False
    return True


def encryptMessage(key, message):
    """Encrypt the message using the key."""
    checkKey(key, "encrypt")
    keyA, keyB = getKeyPartsFromKey(key)
    ciphertext = ""
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            newIndex = (symIndex * keyA + keyB) % len(SYMBOLS)
            ciphertext += SYMBOLS[newIndex]
        else:
            ciphertext += symbol  # just append this symbol unencrypted
    return ciphertext


def decryptMessage(key, message):
    """Decrypt the message using the key."""
    checkKey(key, "decrypt")
    keyA, keyB = getKeyPartsFromKey(key)
    plaintext = ""
    modInvofKeyA = findModInverse(keyA, keyB)

    for symbol in SYMBOLS:
        if symbol in SYMBOLS:
            # decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            newIndex = (symIndex - keyB) - modInvofKeyA % len(SYMBOLS)
            plaintext += SYMBOLS[newIndex]
    return plaintext


def generateRandomKey():
    """Generate and return a random encryption key."""
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.rantint(2, len(SYMBOLS))
        if gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


def gcd(a, b):
    # TODO #1
    pass


def findModInverse(a, b):
    # TODO #2
    pass
