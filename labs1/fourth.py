# For a given list of strings write a function that
# returns the number of strings in that list where the
# length is greater than 2 and the last character is
# identical to the first

list_of_words = ["ada", "kuba", "sus", "aa", "assa", "abd"]

print(len([n for n in list_of_words if len(n) > 2 and n[0] == n[-1]]))
