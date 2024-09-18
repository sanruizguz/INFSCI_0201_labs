# Remove duplicates from a list
def make_set(data):
    new_set=dict.fromkeys(data)
    new_list=list(new_set)
    return new_list

# Making sure is list is also set
def is_set(data):
    new_list=make_set(data)
    if len(new_list) >= len (data):
        return(True)
    else:
        return(False)

# Mergue sets
def union (setA, setB):
    if ((is_set(setA) == True) and (is_set(setB)==True)):
        combined=setA+setB
        no_dupli=make_set(combined)
        return no_dupli
    else:
        return([])

# Intercept sets
def interception (setA, setB):
    if ((is_set(setA) == True) and (is_set(setB)==True)):
        inter = [item for item in setA if item in setB]
        return inter
    else:
        return([])
    
