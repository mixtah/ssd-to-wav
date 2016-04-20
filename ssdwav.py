#
# Author: Michael Bauer
#
import sys,os,wave,time

path = os.path.dirname(os.path.realpath('__file__'))
override = False
recursive = False
input = ""
output = ""
isInputDir = False

def usage():
    print "Converts SSD format file into WAV files. Will convert an individual file or entire directory"
    print "Usage: ssdwav.py <'-r'?> <Input file or directory> <Output Directory?>"
    print "     : ssdwav.py <'-r'?> -o <Input file or directory>"
    print "-r : Process directories recursively and convert all ssd files"
    print "-o : Override .ssd files with produced .wav files"
   
def isSSDFile(file):
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

def convertFile(file):
    #do file convert
    print "TODO"
    
    
def convertDirectory(dir):
    #scan files and convert and save to output
    #if override remove original 
    #call convert directory on each folder if recursive
    print "TODO"

    
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

    
