'''
Developed and Tested with Python 2.7.14 

@author: Alexander Tong
'''
import pandas as pd
import numpy as np

def rng_gen(num, num_list, min, max, type):
    '''
    Description: generates a list of list(s) with random values.
        
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


def gen_col_name(lists, col_orientation):
    '''
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


if __name__ == "__main__":
    #Generate list of list with random values 
    lists = rng_gen(15, 5, 1, 10, randint) 
    
    
    #Example vertical list 
    vertical_col = gen_col_name(lists,'vertical')
    
    df_vertical = pd.DataFrame(np.column_stack(lists), columns = vertical_col)
    
    
    #Example horizontal list 
    horizontal_col = gen_col_name(lists,'horizontal')
    
    df_horizontal = pd.DataFrame(lists, columns = horizontal_col)
    
    
    #sort values in dataframe; both methods execute same
    df_vertical_sort = df_vertical.apply(lambda x: x.sort_values().values)
    
    df_horizontal_sort = pd.DataFrame(np.sort(df_horizontal.values, axis=0), index=df_horizontal.index, columns=df_horizontal.columns)
