def is_power(n):
    if n <=0:
        return False
    if n == 1:
        return True
    if n%4 == 0:
        return is_power(n//4)
    return False
print("Checking 16 : ",is_power(16))
print("Checking 12 : ", is_power(12))
n = int(input("Enter a number : "))
print(is_power(n))