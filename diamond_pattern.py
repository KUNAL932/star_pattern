Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
n=8
>>> def print_pattern():
	for i in range(0,n):
		if (i<4):
			for j in range(i,4):
				print(" ",end="")
			for k in range(0,i):
				print("*",end="")
			for l in range(1,i):
				print("*",end="")
			print("\n")
		else:
			for m in range(4,i):
				print(" ",end="")
			for x in range(i,n):
				print("*",end="")
			for y in range(i,n-1):
				print("*",end="")
			print("\n")

			
>>> print_pattern()
    

   *

  ***

 *****

*******

 *****

  ***

   *

>>> 
