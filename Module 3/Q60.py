# How Will You Set The String Value In Genrateing Random Number
import random

random_number = random.randint(1, 100000)
string_value = "Hello World  "

result = string_value + str(random_number)

print(result)