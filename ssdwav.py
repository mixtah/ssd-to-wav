#
# Author: Michael Bauer
#
import sys,os,wave,time,re

path = os.path.dirname(os.path.realpath('__file__'))
override = False
recursive = False
isInputDir = False
input = ""
output = ""

def usage():
    '''Prints Usage'''
    print "Converts SSD format file into WAV files. Will convert an individual file or entire directory"
    print "Usage: ssdwav.py <'-r'?> <Input file or directory> <Output Directory?>"
    print "     : ssdwav.py <'-r'?> -o <Input file or directory>"
    print "-r : Process directories recursively and convert all ssd files"
    print "-o : Override .ssd files with produced .wav files"
   
def isSSDFile(file):
    '''
    Checks if input string 'file' has the extension .ssd,
    Returns True if so and False otherwise.
    '''
    #check if file ends in .ssd
	if file.split('.')[-1] == 'ssd':
		return True
	else:
		return False

#if the file doesn't exist the application will exit
#will return full path of file if it exists
#will work for files and folders
def validatePath(file):
    if not os.path.exists(file):
        file = os.path.join(path,file)
        if not os.path.exists(file):
            print "The path %s does not exist!" % file
            exit()
    return file


def readSSDHeader(file):
    '''
    Input: file as full path string to file
    Return: A dictionary of variables as keys with values as the values
    '''
    
def getSSDDataStream(file):
    '''
    Input: file as full path string to file
    Return: Reference to the .ssd data as a byte stream
    '''

def fixLogs(file):
    '''
    Locates any labels and meta-data files associated to the given file
    and fixes fixes the meta-data to suit the .wav file.
    '''
    #Locate the .lab and .trg files of the same name
    #this will usually be in a folder called 'labels' if the .ssd is in a folder called 'data'
    # 'labels' and 'data' will have the same parent directory
    #may as well also check current directory if not found in 'labels'
    

def convertFile(file):
    '''
    Input: file as a full directory path to a single file that needs to be converted
    Returns: True if successful, False if unsuccessful
    '''
    #do file convert
    print "TODO"
    
    
def convertDirectory(dir):
    '''
    Input: full directory path that needs to be converted, all applicable files will be
            within this directory. If the recursive option was set, then all subdirectories
            will be searched and all applicable files will be converted
    Returns: Tuple of the form, (Number of detected files, Number of unsuccessful files, Array of Unsuccessful files names )
    '''
    #scan files and convert and save to output
    #if override remove original 
    #call convert directory on each folder if recursive
    print "TODO"

    
if __name__ == '__main__':
    #Point of Entry into script
    if len(sys.argv) <= 4:
        #do file conversion or directory conversion
        #or file conversion with override or directory conversion with override
        #or do recursive directory conversion or override directory conversion
        
        if len(sys.argv)==2:
            #This means it's just a file or directory, no options and output = input
            input = validatePath(sys.argv[1])
            if os.path.isdir(input):
                output = input
            else:
                output = input[0:input.rfind(os.path.sep)]
        else:
            #grab any options if any
            inputPos = 1
            if sys.argv[1]=='-r':
                recursive=True
                inputPos = 2
                if sys.argv[2]=='-o':
                    override=True
                    inputPos = 3
                
            elif sys.argv[1]=='-o':
                override=True
                inputPos = 2
                if sys.argv[2]=='-r':
                    recursive=True
                    inputPos = 3
                    
            input = validatePath(sys.argv[inputPos])
            if not override:
                #we deal with all paths as if they are absolutes (only sith deal in absolutes)
                if os.path.isdir(sys.argv[inputPos+1]):
                    output = os.path.join(path,sys.argv[inputPos+1])
        
        
        #decide if input is file or directory
        isInputDir = os.path.isdir(input)
        
        #Print to user what the program intends to do
        if(isInputDir):
            print "Converting files in directory %s" % input
            if recursive:
                print "and all subdirectories"
                #use this if to decide on output directory if overwrite has been selected
            if override:
                output = input
        else:
            #maybe file isn't .ssd
            if not isSSDFile(input):
                print "The entered file isn't a .ssd file"
                exit()
            print "Converting file %s" % input
            #use this same if to create output folder from file directory
            #if input file is in the working directory of this script then output should be ''
            if override:
                output = input[0:input.rfind(os.path.sep)]
        
        if override:
            print "Old files will be overwritten"
        else:
            print "New files will be placed %s" % output
        
        #Start conversion
        
    else:
        usage()
        exit()
        