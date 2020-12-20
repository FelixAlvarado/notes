import collections

arr = [1,2,3,3,3,4,5,6,2]

print(collections.Counter(arr))

#output Counter({3: 3, 2: 2, 1: 1, 4: 1, 5: 1, 6: 1})

# makes a counter object that shows the array number as the key and and number amount as the value