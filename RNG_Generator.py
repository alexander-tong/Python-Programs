def rng_gen(num, num_list, min, max, type):
    '''
    Description: generates a list of list(s) using built-in random module. 
    
    Args:
        num (int): specify len of list
        num_list (int): specify number of lists to generate 
        min (int): specify min value of range 
        max (int): specify max value of range
        type (str): randint, uniform, random
        
    Returns:
        list of lists 
    '''
    from random import randint
    from random import uniform
    from random import random 

    if num_list == None:
        num_list = 1
        lists = [[] for _ in range(num_list)]
    else: 
        lists = [[] for _ in range(num_list)]
        
        # above is list comprehension; this can be re-written as:
#        lists = []
#        for i in range(num_list):
#            lists.append([]) 
            
    while num > 0:
        for i in lists:
            if type == randint:
                i.append(type(min,max))
            elif type == uniform: 
                i.append(round(type(min,max),2)) 
            elif type == random:
                i.append(round(type(),2)) 
        num -= 1 
    
    return lists 
