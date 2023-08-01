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
list = [19, 1, 9, 3, 10, 13] 
bubbleSort(list) 
print('Sorted array in ascending order:')
print(list)
