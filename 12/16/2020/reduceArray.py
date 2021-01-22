#   Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.
  
  def minSetSize(self, arr: List[int]) -> int:
		# calc len array
        n=len(arr)
		
		# calc half length
        size = n/2
		
		# get counter obj and sort 
        cntr = Counter(arr)
        cntr = sorted(cntr.values())
		
		# initialize delete counter
        del_count = 0
		
		# screen
        if len(cntr) == 1:
            return 1
		
		# process
        while n > size:
            n-= cntr[-1]
            del cntr[-1]
            del_count += 1
        return del_count