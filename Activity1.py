def flip_number(num):
    if num // 10 == 0:
        return num
    last = num%10
    rest = flip_number(num//10)
    return last * pow(10,len(str(rest)))+ rest

print("Number 123 is equal to = ",flip_number(123))
print("Number 456 is equal to = ", flip_number(456))


n = int(input("Enter a number : "))
print(flip_number(n))
