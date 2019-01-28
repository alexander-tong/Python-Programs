'''
Developed and Tested with Python 2.7.14 and ArcMap 10.6

@author: Alexander Tong
'''

import os, traceback, re

if sys.version_info[0] != 2:
    print("This script requires Python version 2.xx")
    sys.exit(1)
    
try:
    import arcpy
    
except ImportError as IE:
    print (IE)
    print ("This script requires arcpy to run")
    sys.exit(1)
    
    
def atoi(text):
    # https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside 
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    # https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside 
    
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


def composite_image_recurve(directory, outfolder, *args):
    '''
    Description: this function will recursively go into a directory and composite a Landsat multispectral image. This 
                 function operates on the default naming convention of Level-1 and Level-2 products. 
                 If composite image already exists, skip. 

    Dependencies: arcpy
    
    Args:
        directory (str): input directory to be parsed. e.g., 'C:\\Users\\EvoEco\\Desktop\\test_img\\'
        outfolder (str): out directory. Specify 'default' to be saved in same folder of input rasters, else specify outpath
        *args (str): currently supports 3 string arguments: 'band', 'sr', 'toa'. 
       
    Returns:
        Output composite Landsat image into desired folder.
        
        $ future implementation:
           - replace arcpy with gdal. 
           - error handling
    ''' 
      
    to_be_processed = []
    
    for arg in args: 
        if arg == 'band':
            to_be_processed.append(arg)
        elif arg == 'sr':
            to_be_processed.append(arg)
        elif arg == 'toa':
            to_be_processed.append(arg) 

    Original_count = 0
    SR_count = 0
    ToA_count = 0
    images = []
    
    for root, dirnames, filenames in os.walk(directory):
        
        # while still in directory, go through files, until exhaust... 
        # out of while loop, process... use a counter 
        Original_count = len(filenames) 
        SR_count = len(filenames) 
        ToA_count = len(filenames) 
        
        try:
            for i in to_be_processed:
                if 'band' in i:
                    print 'processing band'
                    while Original_count > 0:
                        for file in range(len(filenames)): 
                            if 'T1_b' in filenames[file]:
            #                    print filenames[file]
                                images.append(filenames[file])
                                images.sort(key=natural_keys)
                            
                            elif 'RT_b' in filenames[file]:
            #                    print filenames[file]
                                images.append(filenames[file])
                                images.sort(key=natural_keys)
                                
                            #excl. brightness temperature and band quality assessment bands                      
                            for i in range(len(images)):
                                if 'bt' in images[i]:
                                    del images[i]
                                elif 'bqa' in images[i]:
                                    del images[i]
                                
                            Original_count -= 1 
                            
                        left_bracket_remove = str(images).replace('[','')
                        right_bracket_remove = str(left_bracket_remove).replace(']','')
                        quote_remove = str(right_bracket_remove).replace("'",'')
                        add_semi_colon = str(quote_remove).replace(', ',';')
                        
                        images = []
                        
                        #if saving to same folder as input rasters 
                        if 'composite' not in add_semi_colon:
            #               directory = root 
                            arcpy.env.workspace = root 
                            
                            if outfolder == 'default':
                                print root
                                arcpy.CompositeBands_management(add_semi_colon, root + '//' + add_semi_colon[:41] + "composite.tif")
                                print add_semi_colon                    
                            else:
                                print root
                                arcpy.CompositeBands_management(add_semi_colon, outfolder + '//' + add_semi_colon[:41] + "composite.tif")
                                print add_semi_colon    
            #                print root
            #                print add_semi_colon
                        else:
                            print add_semi_colon[:40] + ' is already processed'
    
    #            print root 
    #            print add_semi_colon   
                elif 'sr' in i:
                    print 'processing sr'
                    while SR_count > 0:
                        for file in range(len(filenames)): 
                            if 'sr_band' in filenames[file]:
            #                    print filenames[file]
                                images.append(filenames[file])
                                images.sort(key=natural_keys)
                                
                            #excl. aerosol band and processed NDVI image
                            for i in range(len(images)):
                                if 'aerosol' in images[i]:
                                    del images[i]
                                elif 'ndvi' in images[i]:
                                    del images[i]
                                    
                            SR_count -= 1 
                            
                        left_bracket_remove = str(images).replace('[','')
                        right_bracket_remove = str(left_bracket_remove).replace(']','')
                        quote_remove = str(right_bracket_remove).replace("'",'')
                        add_semi_colon = str(quote_remove).replace(', ',';')
                        
                        images = []
                        
                        if 'composite' not in add_semi_colon:
            #               directory = root 
                            arcpy.env.workspace = root 
        
                            if outfolder == 'default':
                                arcpy.CompositeBands_management(add_semi_colon, add_semi_colon[:44] + "composite.tif")
                                print add_semi_colon                        
                            else:
                                arcpy.CompositeBands_management(add_semi_colon, outfolder + '//' + add_semi_colon[:44] + "composite.tif")
                                print add_semi_colon                    
                        else:
                            print add_semi_colon[:40] + ' is already processed'
                  
            #            print root 
            #            print add_semi_colon   
                elif 'toa' in i:
                    print 'processing toa'        
                    while ToA_count > 0:
                        for file in range(len(filenames)): 
                            if 'toa_band' in filenames[file]:
            #                    print filenames[file]
                                images.append(filenames[file])
                                images.sort(key=natural_keys)
                    
                            ToA_count -= 1 
                            
                        left_bracket_remove = str(images).replace('[','')
                        right_bracket_remove = str(left_bracket_remove).replace(']','')
                        quote_remove = str(right_bracket_remove).replace("'",'')
                        add_semi_colon = str(quote_remove).replace(', ',';')
                        
                        images = []
                        
                        if 'composite' not in add_semi_colon:
            #               directory = root 
                            arcpy.env.workspace = root 
        
                            if outfolder == 'default':
                                arcpy.CompositeBands_management(add_semi_colon, add_semi_colon[:45] + "composite.tif")
                                print add_semi_colon
                            else:
                                arcpy.CompositeBands_management(add_semi_colon, outfolder + '//' + add_semi_colon[:45] + "composite.tif")
                                print add_semi_colon
                        else:
                            print add_semi_colon[:40] + ' is already processed'
                #ignore folders with images that have been processed already 
        except:
                tb = sys.exc_info()[2]
                tbinfo = traceback.format_tb(tb)[0]

                # Python Errors(s)
                pymsg = 'PYTHON ERRORS:\nTraceback info:\n' + tbinfo +'\nErrorInfo:\n' +\
                        str(sys.exc_type) + ':' + str(sys.exc_value) + '\n'

                # Arcpy Error(s)       
                arcpy.AddError(pymsg)
                msgs = 'Arcpy ERRORS:\n' + arcpy.GetMessages(2) + '\n'

                # Print Error(s)
                print (pymsg + '\n')
                print (msgs) 
                
                pass


if __name__ == "__main__":
        
    directory = r'<insert in folder path>'
    outfolder = r'<insert out folder path>'        
    
    composite_image_recurve(directory,outfolder,'band','sr','toa')   
    
    
