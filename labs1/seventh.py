# Write a program that opens a file containing two
# columns and save it as a dictionary where the
# values of the first column are the keys for values in
# the second column
from urllib import request

url = "https://wp.faculty.wmi.amu.edu.pl/lista.txt"
data = request.urlopen(url)
slownik = {}

for line in data:
    slownik[line[:6].decode('ISO-8859-2')] = line[7:-2].decode('ISO-8859-2')

print(slownik)
