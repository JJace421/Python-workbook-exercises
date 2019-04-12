letter = input("Letter: ")
vowel = ["a","e","i","o","u"]

if letter in vowel:
    print("Vowel")
elif letter == "y":
    print("Vowel and consonant")
else:
    print("Consonant")
