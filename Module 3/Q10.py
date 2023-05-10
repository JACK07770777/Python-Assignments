# Write A Python Function  That Takes  Two List  And Return True If They Have At Least One Common member ?


# def lists(l1,l2):
    
#     end=False
#     for x in range l1:
#         for y in range l2:
#             if x==y:
#                 end==True
#                 return end
                
# print(lists([1,2,3,4,5],[1,2,3,4,5]))     
        
               
#11. Write a Python function that takes two lists and returns True if they have at least one common member. 
def common_data(l1, l2):
     result = False
     for x in l1:
         for y in l2:
             if x == y:
                #  result = True
                 if result==True:
                     print("There Is One Common Member So Answer Is True")
                 else:
                     print("Try Another")
                        
                #  return result
print(common_data([1,2,3,4,5], [85,6,7,8,9]))
# print(common_data([1,2,3,4,5], [6,7,8,9]))