# Write A Python Program that user to enter only odd numbers,else will raise an exception ?

def odd_numbers(maximum):
    return_string = ""

    # Set the range to start from 1 and include only odd numbers up to the maximum.
    for num in range(1, maximum+1, 2):

        # Append the odd number and a space to the return string.
        return_string += str(num) + " "


    if return_string == "":
        return "No numbers displayed"
    else:
        return return_string.strip()  


print(odd_numbers(6)) 
print(odd_numbers(10)) 
print(odd_numbers(1))  
print(odd_numbers(3))  
print(odd_numbers(0))   