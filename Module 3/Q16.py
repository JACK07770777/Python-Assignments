# Write A python Program To Get Unique Values From List ?
# li=[1,2,3,4,5,6,]
# x=li.append(2)
# print(x)

# def unique(l1):
#     x=set(l1)
#     y=(list(x))
#     for i in y:
#         print(i)
# l1=[1,2,3,4,5,6,7,8,9,10] 
# print("The Unique Values From List")
# unique(l1)
       
       
def unique(l1):
 
    # insert the list to the set
    l_set = set(l1)
    # convert the set to the list
    u_list = ((l_set))
    for x in u_list:
        print (x),
 
 
# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)       