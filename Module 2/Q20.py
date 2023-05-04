# Write A Python Function To Reverses A String If Its length Is Multiple Of 4 ?
def reverse_string(str1):
    print("Enter Any Two word")
    str1=str(input("enter Any word"))
    if len(str1) % 4 == 0:
        return ''.join(reversed(str1))
    return str1


# print(reverse_string('abcd'))
# print(reverse_string('python'))
# str1=str(input("Enter  First String:-->"))
print(reverse_string())