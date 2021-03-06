def highestProductof3(array):
	if len(array) < 3:
	    return 'There must be at least 3 elements!'

	highest = []
        for i in xrange(2):
	   max_elem = max(array)
	   highest.append(max_elem) 
	   array.remove(max_elem)
	   
	count = 0
	for num in array:
	    if num<0:
		count+=1
		
	if count >0:
	    lowest_elem = []
	    for i in xrange(2):
		min_elem = min(array)
		lowest_elem.append(min_elem)
		array.remove(min_elem)
	    return max(highest)*lowest_elem[0]*lowest_elem[1]
        else:
	    return max(array)*highest[0]*highest[1]
	    
	    
	    
	  
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest =  min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # except this one--we pre-populate it for the first /3/ items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # walk through items, starting at index 2
    for current in list_of_ints[2:]:

        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_three
