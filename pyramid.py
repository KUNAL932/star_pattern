Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
n=8
>>> for i in range(0,n):
	for k in range(i,n):
		print(" ",end="")
	for j in range(0,i):
		print("*",end="")
	for i in range(1,i):
		print("*",end="")
	print("\n")

        

       *

      ***

     *****

    *******

   *********

  ***********

 *************

######################################################################################################

>>> for i in range(0,n):
	for j in range(0,i):
		print(" ",end="")
	for k in range(i,n):
		print("*",end="")
	for m in range(i,n-1):
		print("*",end="")
	print("\n")

	
***************

 *************

  ***********

   *********

    *******

     *****

      ***

       *

>>> 
