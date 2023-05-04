# Write A python Program To  Add "ing" At the End Of A Given String ?

# Length Sould Be At Least 3 If The Given string already Ends With "ing" Then Add "ly" insred If The String Length of The 
# GivenString Is Les Then 3 ,Leave It Unchanged


# add_ing=str(input("Enter any String"))
string=str(input("Enter Any String For Adding ing"))


def add_ing(string):
    if (len(string) > 2):
        if ((string[-1] == 'g') and (string[-2] == 'n') and (string[-3] == 'i')):
            return (string + 'ly')
        else:
            return (string + 'ing')
    else:
        return (string)



# print(add_ing('pingpong'))
print(add_ing(string))