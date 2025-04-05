import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(chosen_direction):

    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_index = alphabet.index(letter) + shift_amount
                shifted_index %= len(alphabet)
                cipher_text += alphabet[shifted_index]
        print(f"Here is the encoded result: {cipher_text}")

    def decrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_index = alphabet.index(letter) - shift_amount
                shifted_index %= len(alphabet)
                cipher_text += alphabet[shifted_index]
        print(f"Here is the decoded result: {cipher_text}")

    if chosen_direction == "encode":
        encrypt(text, shift)

    if chosen_direction == "decode":
        decrypt(text, shift)


leave = False
while leave is False:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction)
    user_continue = input("type yes if you want to go again: ")
    if user_continue != "yes":
        leave = True
