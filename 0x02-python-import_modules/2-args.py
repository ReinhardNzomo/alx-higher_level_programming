#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	list_arg = []
	if len(sys.argv) == 1:
	    print('0 arguments.')

	else:
	    for x in sys.argv:
	        list_arg.append(x)
    
 	   if (len(sys.argv) == 2):
 	       print('1 argument:')
 	       print('1: {}'.format(list_arg[1]))
    
 	   else:
 	       print('{} arguments:'.format(len(sys.argv) - 1))
  	      for x in range(len(sys.argv)):
        	    if (x > 0):
                	print('{}: {}'.format(x, list_arg[x]))
