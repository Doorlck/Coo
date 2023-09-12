def binary_search(sorted_array,search_val):
    lower_bound = 0
    upper_bound = len(sorted_array)-1

    while lower_bound <= upper_bound:
        midpoint= (upper_bound +lower_bound)//2

        value_mid = sorted_array[midpoint]

        if search_val == value_mid:
            return midpoint
        elif search_val < value_mid :
            upper_bound = midpoint-1
        else:
            lower_bound = midpoint+1
        
    return None

a= binary_search([3,7,15,80,202],202)
print(a)


