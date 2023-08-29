
# class Solution:
#     #Function to partition the array around the range such 
#     #that array is divided into three parts.
# 	def threeWayPartition(self, array, a, b):
# 	    # code here
# 	    start = 0
# 	    end = len(array) - 1
# 	    i = 0
# 	    def swap(array, i, j):
# 	       array[i], array[j] = array[j], array[i]
# 	    while i <= end: 
# 	        if array[i] < a:
# 	            swap(array, i, start)
# 	            i += 1
# 	            start += 1
# 	        elif array[i] > b:
# 	            swap(array, i, end)
# 	            end -= 1
# 	        else:
# 	            i += 1
	   
# 	   #start = []
# 	   #mid = []
# 	   #end = []
	   
# 	   #for i in range(len(array)):
# 	   #    if array[i] < a:
# 	   #        start.append(array[i])
# 	   #    elif array[i] > b:
# 	   #        end.append(array[i])
# 	   #    else:
# 	   #        mid.append(array[i])
	           
# 	   #array[::]=start+mid+end
	           
	           
