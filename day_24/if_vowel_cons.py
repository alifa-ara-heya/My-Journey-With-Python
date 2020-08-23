# day 24
# 23- August- 2020
# sohoj vashay python

print("Please, input the character, I will tell you whether it's vowel or consonant: ")
character = input().lower()

if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print("Vowel")
else:
    print("Consonant")


# author's way:
print("Please, input the character: ")
character = input()

if character >= 'a' and character <= 'z' or character >= "A" and character <='Z':
    if character in 'aeiouAEIOU':
        print("Vowel")
    else:
        print("Consonant")
else:
    print('Nothing')