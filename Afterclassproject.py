# part 1 reversed number
def flip_number(num):
    if num // 10 == 0:
        return num
    last = num%10
    rest = flip_number(num//10)
    return last * pow(10,len(str(rest)))+ rest

print("Number 123 is equal to = ",flip_number(987))
print("Number 456 is equal to = ", flip_number(1084))


s = int(input("Enter a number : "))
print(flip_number(s))

# part 2 reversed name
def flip_name(o):
    if len(o) == 1:
        return o
    return flip_name(o[1:]) + o[0]
print("A reverse of Hannah is : ", flip_name("Hannah"))
print("A reverse of Codingal is : ",flip_name("Codingal"))
p = (input("Enter a name : "))
print(flip_name(p))

# part 3 power of 4
def is_power(d):
    if d <=0:
        return False
    if d == 1:
        return True
    if d%4 == 0:
        return is_power(d//4)
    return False
print("Checking 32 : ",is_power(16))
print("Checking 9 : ", is_power(12))
i = int(input("Enter a number : "))
print(is_power(i))
