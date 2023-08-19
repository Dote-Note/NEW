# Bubble sort: Python implementation by Abel
def bubbleSort(list): 
  isSwapped = True 

while isSwapped:
isSwapped = False 
for i in range(len(list) - 1):
   if list[i] > list[i + 1]:
isSwapped = True
list[i], list[i+1] = list[i+1], list[i] 

# Test bubble sort 
list = [29.2, 71, 98, 78, 62, 29.1] 
bubbleSort(list) 
print('Sorted array in ascending order:')
print(list)
