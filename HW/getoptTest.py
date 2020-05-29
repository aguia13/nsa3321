import sys
import getopt 

getopt.getopt('-a arg'.split(),'a:')					#a expects an arg
getopt.getopt('-a arg'.split(),'a:b')					#no b, no problem
getopt.getopt('-b arg -a my-file.txt'.split(),'ab:')	#my-file.txt is arg, not option
getopt.getopt('-a arg --output=other-file.txt my-file.txt'.split(),'a:b',['output=']) #long options

def usage():
	print("""usage: my_program.py -[abh] file1,file2,...""")

opts, args = getopt.getopt(sys.argv[1:],'abh')

opt_dict = dict(opts)

if 'h' in opt_dict:
	usage()