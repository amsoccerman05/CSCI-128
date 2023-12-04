#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 9
#   References: no one
#   Time: 3 hours

# function for caesar cipher encryption
def encrypt(message, shift):
    encrypted_message = ""  # empty string to store encrypted message
    for char in message:  # iterate through each letter
        if char.isalpha():  # check if char is in alphabet
            is_upper = char.isupper()  # check if char is uppercase
            char = char.lower()  # convert to lowercase
            char_code = ord(char)  # get Unicode point of the character
            char_code = (char_code - ord('a') + shift) % 26  # apply the shift
            char = chr(char_code + ord('a'))  # convert code back
            if is_upper:  # if the original character was uppercase
                char = char.upper()
        encrypted_message += char  # add the character to the encrypted message
    return encrypted_message  # return the encrypted message


# function for caesar cipher decryption
def decrypt(text, keyword):
    for shift in range(26):  # try all possible shifts
        decrypted_message = ""  # initialize an empty string to store the decrypted message
        for char in text:  # iterate through each character in the encrypted text
            if char.isalpha():  # check if the character is in the alphabet
                is_upper = char.isupper()  # check if the character is uppercase
                char = char.lower()  # convert the character to lowercase
                char_code = ord(char)  # get the Unicode code point of the character
                char_code = (char_code - ord('a') - shift) % 26  # apply the Caesar cipher shift
                char = chr(char_code + ord('a'))  # convert the shifted code point back to a character
                if is_upper:  # if the original character was uppercase
                    char = char.upper()  # convert the character back to uppercase
            decrypted_message += char  # add the character to the decrypted message
        if keyword.lower() in decrypted_message.lower():  # check if the keyword is found in the decrypted message
            return [decrypted_message, shift]  # return the decrypted message and shift
    return "ERROR"  # return "ERROR" if the keyword is not found for all shifts



# test for encryption function
def test_encrypt(word, shift, expected):
    encrypted = encrypt(word, shift)  # call the encrypt function
    assert encrypted == expected  # check if the result matches the expected output


# test for decryption function
def test_decrypt(word, keyword, expected_word, expected_shift):
    result = decrypt(word, keyword)  # call the decrypt function
    if result == "ERROR":  # if decryption fails, check for an error
        assert result == expected_word  # check if the error message matches the expected output
    else:
        decrypted_word, shift = result  # get the decrypted word and shift
        assert decrypted_word == expected_word  # check if the decrypted word matches the expected output
        assert shift == expected_shift  # check if the shift matches the expected shift


if __name__ == '__main__':
    option = int(input("option> "))  # get the user's choice (1, 2, or 3)

    if option == 1:  # if the user chooses encryption
        message = input("MESSAGE> ")  # get the message to encrypt
        shift = int(input("SHIFT> "))  # get the shift value
        encrypted_message = encrypt(message, shift)  # call the encrypt function
        print("OUTPUT", encrypted_message)  # print the encrypted message

    elif option == 2:  # if the user chooses decryption
        encrypted_message = input("MESSAGE> ")  # get the encrypted message
        keyword = input("KEY> ")  # get the keyword
        result = decrypt(encrypted_message, keyword)  # call the decrypt function
        if result == "ERROR":  # if decryption fails
            print("OUTPUT ERROR")  # print an error message
        else:
            decrypted_message, shift = result  # get the decrypted message and shift
            print("OUTPUT", decrypted_message)  # print the decrypted message
            print("OUTPUT", shift)  # print the shift

    elif option == 3:  # if the user chooses testing
        # run the test cases for encryption and decryption
        test_encrypt("My secret message", 10, "Wi combod wocckqo")
        test_encrypt("N0t numb3r5", 7, "U0a ubti3y5")
        test_encrypt("Large negative shift", -82, "Hwnca jacwpera odebp")
        test_decrypt("Ger csy vieh xlmw?", "read", "Can you read this?", 4)
        test_decrypt("Ujqhlgyjshzq ak fwsl!", "is", "Cryptography is neat!", 18)
        test_decrypt("Ujqhlgyjshzq ak fwsl!", "message", "ERROR", 0)
