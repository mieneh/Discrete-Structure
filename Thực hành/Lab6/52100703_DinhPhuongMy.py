import math

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#Exercise 1:
def nextPrime(n):
    num = n + 1  
    while True:
        if isPrime(num):
            return num
        num += 1  
print("\nExercise 1")
n = [3, 8]
for i in n:
    print("Next Prime of {}: {}".format(i, nextPrime(i)))

#Exercise 2:
def primeFact(p):
    factors = []
    while p % 2 == 0:
        factors.append(2)
        p = p // 2
    for i in range(3, int(p**0.5) + 1, 2):
        while p % i == 0:
            factors.append(i)
            p = p // i
    if p > 2:
        factors.append(p)
    return factors
print("\nExercise 2")
n = [30, 60]
for i in n:
    print("Prime fact of {}: {}".format(i, primeFact(i)))

#Exercise 3:
def printPrime(N):
    print("Print prime of {}:".format(N))
    for num in range(2, N):
        if isPrime(num):
            print(num)
print("\nExercise 3")
n = [20, 40]
for i in n:
    printPrime(i)

#Exercise 4:
def contestAlgorithm(n):
    if n < 2:
        return []
    else:
        O = [2]
        i = 3
        while i + 2 < n:
            flag = True
            j = 0
            while j + 1 < len(O):
                if i % O[j] == 0:
                    flag = False
                    break
                j += 1
            if flag:
                O.append(i)
            i += 2
        return O
print("\nExercise 4")
n = [5, 10, 20]
for i in n:
    print("Result for n = {}: {}".format(i, contestAlgorithm(i)))

#Exercise 5:
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print("\nExercise 5")
n = [[24, 40], [36, 48]]
for i in n:
    print("GCD of", i[0], "and", i[1], ":", gcd(i[0], i[1]))

#Exercise 6:
def lcm(a, b):
    gcd_result = gcd(a, b)
    lcm_result = (a * b) // gcd_result
    return lcm_result
print("\nExercise 6")
n = [[12, 18], [10, 20]]
for i in n:
    print("LCM of", i[0], "and", i[1], ":", lcm(i[0], i[1]))

#Exercise 7:
def base10_to_base2(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary
print("\nExercise 7")
n = [5, 15]
for i in n:
    print("Binary representation of {}: {}".format(i, base10_to_base2(i)))

#Exercise 8:
def decimal_to_binary_fraction(n):
    binary = ""
    while n > 0:
        n = n * 2
        if n >= 1:
            binary += "1"
            n = n - 1
        else:
            binary += "0"
    return binary
print("\nExercise 8")
n = [0.5, 0.25]
for i in n:
    print("Binary representation of {}: {}".format(i, decimal_to_binary_fraction(i)))

#Exercise 9: 
def decimal_to_hexadecimal(n):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        remainder = n % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        n = n // 16
    return hexadecimal
print("\nExercise 9")
n = [255, 1024]
for i in n:
    print("Hexadecimal representation of {}: {}".format(i, decimal_to_hexadecimal(i)))

#Exercise 10: 
def convertbase(a, base1, base2):
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    for digit in a:
        decimal = decimal * base1 + digit
    result = []
    while decimal > 0:
        remainder = decimal % base2
        result.insert(0, remainder)
        decimal = decimal // base2
    if not result:
        result.append(0)
    if base2 == 16:
        hexadecimal = ""
        for digit in result:
            hexadecimal += hex_chars[digit]
        return hexadecimal
    return result
print("\nExercise 10")
n = [[[1, 1, 1], 10, 16], [[1, 0, 1, 1], 2, 10], [[2, 5, 6], 8, 16]]
for i in n:
    print("Converted representation of {} from base {} to base {}: {}".format(i[0], i[1], i[2], convertbase(i[0], i[1], i[2])))