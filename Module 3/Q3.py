# #  Differnitiate Between Append() And Extend () Method?
# 1. Append - will only add a single element to the list - Be it a single element, a list or tuple etc.

# 2. Extend - will add all elements of an iterable to the list - It throws an error if you try to extend using a single element. Do note a str or single char will be considered a list, so that will work.

x=[1,12,19,26,29]
x.append([1,2])
print(x)


a=[10,9,8,7,6,5]
a.extend([4,3])
print(a)