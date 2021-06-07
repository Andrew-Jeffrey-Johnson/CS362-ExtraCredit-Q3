def add_finder(array, target_sum):
    for x in array:
        for y in array:
            if (x+y==target_sum):
                return [x,y]
    return []
