import sys,os,wave,time

def usage():
	print "ssdwav.py <Input file or directory> <Output file or directory>"

def isSSDFile(file):
	if file.split('.',1)[1] == 'ssd':
		return True
	else:
		return False

if len(sys.argv) != 2
