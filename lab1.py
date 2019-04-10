
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == None: 
        raise ValueError
    maxval = 0
    for i in range(0, len(int_list)-1, 1):
        if (int_list[i] > maxval):
            maxval = int_list[i]
    return maxval 

def reverse_rec(int_list):   # must use recursion
    if int_list == None:
        raise ValueError
    return [] if not int_list else int_list[-1:] + reverse_rec(int_list[:-1])   

def bin_search(target, low, high, int_list):  # must use recursion
    if int_list == None:
        raise ValueError
    elif int_list == []:
        return None
    else:
        mid = int((high+low)/2)
    
    if(int_list == None):
        raise ValueError

    if (int_list[mid] == target):
        return mid
    if (low >= high):
        return None
    if(int_list[mid] > target):
        return bin_search(target, low, mid-1, int_list)
  
    if(int_list[mid] < target):
        return bin_search(target, mid+1, high, int_list)
    
