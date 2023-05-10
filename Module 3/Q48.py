# Write a python program to combine values in python list of dictionaries.
# Sample data [{"item":"item 1"},{"amount":400},{"item":"item 2"},{"amount":300c}]
# {"item":"item1","amount":750}
# Expected Output: Counter({"item1":1150,},{"item2":300})

# data = [{"item":"item 1"},{"amount":400},{"item":"item 2"},{"amount":300},{"item":"item 1"},{"amount":750}]

# result = Counter()
# for d in data:
#     for key, value in d.items():
#         if key == 'item':
#             result[value] += 0
#         elif key == 'amount':
#             result[data[data.index(d) - 1]['item']] += value

# print(result)
data = [{"item":"item 1"},{"amount":400},{"item":"item 2"},{"amount":300},{"item":"item 1"},{"amount":750}]

result = {}
current_item = None

for d in data:
    for key, value in d.items():
        if key == 'item':
            current_item = value
            if current_item not in result:
                result[current_item] = 0
        elif key == 'amount':
            if current_item:
                result[current_item] += value

print(result)