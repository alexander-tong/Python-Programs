def gen_col_name(lists, col_orientation):
    ''''
    Description:
        Creates list of titles to len(list) or list[i]. 
        Supports up to len 676 header names (i.e., permutations corresponding to 26*26 letters of alphabet)
        
    Args:
        lists (list): type must be list of int, float, string
        col_orientation: horizontal; headers generated based on len(list)
                         vertical; headers generated based on number of lists within list of lists
                              
    Returns:
        headers for list of lists 
    '''
    base = 'col' 
    alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alpha_split = alpha.split(' ') 
    alpha_split_greater_than_26 = alpha.split(' ')  
    alpha_split_extend = alpha.split(' ')        
    count = 0
    combined_title = []  
    
    if col_orientation == 'horizontal': 
        length_list = len(lists[0])
    elif col_orientation == 'vertical':
        length_list = len(lists)
        
    if length_list < 26:
        if col_orientation == 'horizontal':
            while len(lists[0]) != len(alpha_split):
                alpha_split.pop()
                
        elif col_orientation == 'vertical':
            while len(lists) != len(alpha_split):
                alpha_split.pop()
            
        for i in range(len(alpha_split)):
            combined_title.append(base + ' ' + alpha_split[i])    
            
    #support > len 27 values specified 
    #reset every 27, such that aa... az...; ba... bz;
    else:
        #since a... z is len 26, subtract 
        length = length_list - 26
                
        while length > 0:
            for i in range(length):
                alpha_split.append(alpha_split_greater_than_26[0] + alpha_split_extend[0])
                del alpha_split_extend[0]
                length -= 1
                count += 1
                if count == 26:
                    count = 0
                    alpha_split_extend = alpha.split(' ') 
                    del alpha_split_greater_than_26[0]
         
        for i in range(len(alpha_split)):
            combined_title.append(base + ' ' + alpha_split[i]) 
    
    return combined_title 
