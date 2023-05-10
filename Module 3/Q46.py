# Write A Python Program To Create and Disply  All Combinations Of Letters Selecting
# Each Letter  From A Different key In A Dictionary.
# Sample Data:{"1":["a","b"],'2':["c","d"]}
# expected Output:-> ac ad bc bd 


test_dict = {"1":["a","b"],"2":["c","d"]} 
  
combinations = [p+q for p in test_dict["1"] for q in test_dict["2"]] 
  
print("All combinations are: " + str(combinations))         