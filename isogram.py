def is_isogram(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram(""))
print(is_isogram("αβγα"))