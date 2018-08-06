'''
Developed and tested in Python 3.4.3 

@author: Alex
'''

def main():
    '''
    Description: Program asks the user for a textfile name and prints the number of characters, words, and lines from that textfile.
    '''
    import os
    
    os.chdir('Specify pathname')		#initialize me before use
    userfile = input("Specify textfile name: ")	#ensure extension of textfile is included 

    done = False
    while not done: 
        infile = open(userfile,'r')
        print("There are %d characters in this textfile" % (char(infile)))
        infile.close()

        infile = open(userfile,'r')
        print("There are %d words in this textfile" % (words(infile)))
        infile.close()

        infile = open(userfile,'r')
        print("There are %d lines in this textfile" % (lines(infile)))
        infile.close()
        done = True
        
    infile.close()

# Reads each character in the file 
def char(infile):
    count = 0
    for line in infile:   
        parts = line.split() 
        for i in parts: 
            total = len(i)
            count += total
    return count

# Reads each word in the file                
def words(infile):
    count = 0
    for line in infile:   
        parts = line.split() 
        for i in range(len(parts)):
            count += 1 
    return count

# Reads each line in the file 
def lines(infile):
    count = 0
    for line in infile:
        count += 1
    return count

main()
