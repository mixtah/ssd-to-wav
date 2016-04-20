import sys,os,wave,time

def usage():
    print "Converts SSD format file into WAV files. Will convert an individual file or entire directory"
	print "Usage: ssdwav.py <'-r'?> <'-o'?> <Input file or directory> <Directory>"
    print "-r : Process directories recursively and convert all ssd files"
    print "-o : Override .ssd files with produced .wav files (Doesn't require output directory)"
   
def isSSDFile(file):
    #check if file ends in .ssd
	if file.split('.')[-1] == 'ssd':
		return True
	else:
		return False

#Used to decide between converting a directory full of files or a single file
def isDirectory(directory):
    #check if last part in directory doesn't have a file extension
    if len(directory.split(os.path.sep)[-1].split('.'))==1:
        return True
    else:
        return False

if len(sys.argv) == 3:
    #do file conversion or directory conversion
    #or file conversion with override or directory conversion with override
    
elif len(sys.argv) == 4:
    #do recursive directory conversion or override directory conversion
    
else:
    usage()
    exit()

    
