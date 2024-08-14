



## Sequential Search
#def Sequential_Search(dlist, item):

#    pos = 0
#    found = False
    
#    while pos < len(dlist) and not found:
#        if dlist[pos] == item:
#            found = True
#        else:
#            pos = pos + 1
    
#    return found, pos

#print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],65))


## Validate Anagrams
#def anagram(word1, word2):
#    word1 = word1.lower()
#    word2 = word2.lower()
#    return sorted(word1) == sorted(word2)

#print(anagram("cinema", "iceman"))
#print(anagram("cool", "loco"))
#print(anagram("men", "women")) # returns false


# Recursive Binary Search (must be sorted first)
# Time: O(log n)

## Returns index of x in arr if present, else -1
#def binary_search(arr, low, high, x):
 
#    # Check base case
#    if high >= low:
 
#        mid = (high + low) // 2
 
#        # If element is present at the middle itself
#        if arr[mid] == x:
#            return mid
 
#        # If element is smaller than mid, then it can only
#        # be present in left subarray
#        elif arr[mid] > x:
#            return binary_search(arr, low, mid - 1, x)
 
#        # Else the element can only be present in right subarray
#        else:
#            return binary_search(arr, mid + 1, high, x)
 
#    else:
#        # Element is not present in the array
#        return -1

## Test array
#arr = [ 2, 3, 4, 10, 40 ]
#x = 40
 
## Function call
#result = binary_search(arr, 0, len(arr)-1, x)
 
#if result != -1:
#    print("Element is present at index", str(result))
#else:
#    print("Element is not present in array")

#    # Create a binary search algorithm (recursive)

#    def binary_search(arr, target, low, high):
#        if high >= low:
#            mid = low + high // 2
#        if arr[mid] == target:
#            return target
#        elif target < mid:
#            return binary_search(arr, target, low, mid-1)
#        elif target > mid:
#            return binary_search(arr, target, mid+1, high)
#        else:
#            return -1

# Hash Tables
class hashtable:
    def __init__(self, items):
        self.bucket_size = len(items)
        self.buckets = [[] for i in range(self.bucket_size)]
        self.assign_buckets(items)

    def assign_buckets(self, items):
        for key, value in elements:
            hash_value = hash(key)
            index = hash_value % self.bucket_size
            self.buckets[index].append((key, value))
            
    def get_value(self, input_keys):
        hash_value = hash(input_keys)
        index = hash_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_keys:
                return(value)


        
  