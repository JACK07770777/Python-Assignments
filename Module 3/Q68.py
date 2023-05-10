# Write A Python Program To  Return Sum Of all divisors of a number ?
def sum_of_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)
    
# Example usage:
print(sum_of_divisors(10)) # 1 + 2 + 5 + 10 = 18
print(sum_of_divisors(15)) # 1 + 3 + 5 + 15 = 24