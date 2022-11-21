# kümnendsüsteem - kahendsüsteem
# Aleksander Pulver

import sys

binary = '$'
n = 15
try: 
    input = int(input("Sisesta kümnendsüsteemi number? "))
    limit = 2**(n + 1)
    input <= limit
except ValueError:
    print("Palun sisesta täisarv", limit)
    sys.exit()

while n >= 0:
    if input < 2**n:
        binary = binary + '0'
    else:
        binary = binary + '1'
        input = input - 2**n
    n = n - 1
print(binary)
