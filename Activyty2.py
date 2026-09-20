def flip_name(s):
    if len(s) == 1:
        return s
    return flip_name(s[1:]) + s[0]
print("A reverse of Maya is : ", flip_name("Maya"))
print("A reverse of Code is : ",flip_name("Code"))
n = (input("Enter a name : "))
print(flip_name(n))