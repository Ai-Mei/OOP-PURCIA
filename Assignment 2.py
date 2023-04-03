# Princess Mae F. Purcia
# BSCPE 1-4
# Assignment 2 Problem 2


import pyfiglet

# DECRYPTION
# Introduction
print ("=" * 150)
result = pyfiglet.figlet_format("DECRYPTION", font = "kban")
print(result)
print ("=" * 150)
print()

print("\33[31m               ／＞　 フ\33[0m".center(50))
print("\33[31m               | 　_　_| \33[0m".center(50))
print("\33[31m          ／` ミ＿xノ \33[0m".center(50))
print("\33[31m         /　　　　 |\33[0m".center(50))
print("\33[31m        /　 ヽ　　 ﾉ\33[0m".center(50))
print("\33[31m        │　　|　|　|\33[0m".center(50))
print("\33[31m／￣|　　 |　|　|\33[0m".center(50))
print("\33[31m(￣ヽ＿_ヽ_)__)\33[0m".center(50))
print("\33[31m＼二\33[0m".center(50))
print("\33[35m \n Hi, this is \33[31mDecrypMate\33[0m. \33[35mI am designed to help you decrypt your messages. \n\33[0m".center(150))
print(" 🐾   " * 20)
print()



# Make the user interact to start the program.
start = int(input("\33[33mAre you ready to decrypt your message with me? If so, please \33[31mpress 1\33[33m to continue and if you want to know more about me, please feel free to \33[31mpress 2. \n\33[0m"))
while start  == 2:
    print()
    print("‧₊˚⋅♡𓂃 ࣪ ִֶָ☾."* 10)
    print()
    print("\33[34mIt seems that you want to know more about me  \33[31m꒰ ˶• ༝ •˶꒱ .\33[34m Don't worry, I am more than willing to explain \33[31mପ(๑•ᴗ•๑)ଓ ♡ . \33[0m".center(150, " "))
    print("\33[36mFirst, I will ask you an encrypted message. Then I will try to help you to decrypt your message and show you the decrypted message.\33[0m".center(150, " "))
    print()
    print("‧₊˚ ⋅♡𓂃 ࣪ ִֶָ☾." * 10)
    print()
    start = int(input("\33[35mNow, I hope I brought light to you. If you are now ready to decrypt messages with me, hit the \33[31m1 button. \n\33[0m"))
    print()



# Import string function to generate our key values and assign key.
import string

# Assign key as the original character of the user's input.
key = " " + string.punctuation + string.digits + string.ascii_letters

# Generate the values of key as list.
key = list(key)

# Copy the key and assign it as key_values.
key_values = " " + string.punctuation + string.digits + string.ascii_letters

# Generate a list with the elements of key_values.
key_values = list(key_values)



# Identify the index of the key and assign the equivalent key_values.
# Substitute every ! to u. Since the index of ! in the list is 1:
key_values [1] = "u"

# Substitute every # to i. Since the index of # in the list is 3:
key_values [3] = "i"

# Substitute every & to e. Since the index of & in the list is 6:
key_values [6] = "e"

# Substitute every * to a. Since the index of * in the list is 10:
key_values [10] = "a"

# Substitute every + to a. Since the index of + in the list is 11:
key_values [11] = "o"



# Ask for the user's message thru input function. Save the input as user_input.
print()
print("\33[33m\nLet's go \33[31mฅ(•ิo•ิ)ฅ\n\33[0m")
print()
print()

user_input = input("\33[31mPlease type in a message to decrypt: \n\33[0m")
print()
print()
print()
result = pyfiglet.figlet_format("Please wait...", font = "straight" )
print(result)
print("\33[32mᶻ 𝗓 𐰁\33[0m" *5)
print()



# Initialize a variable reserved for the decrypted message. Save it as cipher_text.
cipher_text = ""

# Assign a variable index to find the index of the key.
# And since, we changed the values of the of the key_values, we assign the variable cipher_text to save the new key value.
for letter in user_input:
        index = key.index(letter)
        cipher_text += key_values[index]

# Print the original message and the decrypted message.
print("\33[34mThe message you inputted: \33[0m" , user_input)
print("\33[34mThe decrypted message: \33[0m" , cipher_text)

print()
print()
print("\33[31m /ᐠ - ˕ -マ♡ ꒱ ˎ\33[0m")
print("\33[33mThank you for spending your time with me. Let us meet again if you wish to decrypt more messages in the future! Keep on cracking the mysteries of the world! \nLove, DecrypMate.\n")




# Ai, Mei ✩