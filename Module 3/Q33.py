# Write A Python Script To Sort (Asscending And Descing) A Dictionary By Value ?
# Ascending sort
def sort_dict_asc(d):
  return sorted(d.items(), key=lambda x: x[1])

def sort_dict_desc(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)
  
d = {'A': 1, 'B': 2, 'C': 3}