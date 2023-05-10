# write A Python  Program to  find the maximum and minimum numbers from the specified decimal numbers.
def max_min_decimal_numbers(decimal_numbers):
    max_num = decimal_numbers[0]
    min_num = decimal_numbers[0]
    for num in decimal_numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return (max_num, min_num)

# Example usage:
decimal_numbers = [3.5, 2.8, 4.1, 1.9, 5.2]
print(max_min_decimal_numbers(decimal_numbers))