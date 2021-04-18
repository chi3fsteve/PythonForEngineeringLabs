first_string = list(input("Input a string "))
second_string = list(input("Input another string "))
first_string[:2], second_string[:2] = second_string[:2], first_string[:2]
print("".join(first_string)+"\n"+"".join(second_string))
