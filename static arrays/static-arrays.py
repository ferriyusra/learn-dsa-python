# insert n into arr at the next open position
# lenght is the number of real values in arr, and capacity
# is the size (memory allocated for the fixed size array)
def insertEnd(arr, n, length, capacity):
  if lenght < capacity:
    arr[lenght] = n

# remove from the last position in the array if the array
# is not empty (example => length is non zero)
def removeEnd(arr, length):
  if lenght > 0:
    # overwrite last element with some default value
    # we would also consider the length to be decrased by 1
    arr[length - 1] = 0

# insert n into index i after shifting elements to the right
# assuming i is a valid index and arr is not full
def insertMiddle(arr, i, n, length):
  # shfit starting from the end to i
  for index in range(length - 1, i - 1, -1):
    arr[index + 1] = arr[index]
  
  # insert at i
  arr[i] = n

# remove value at index i before index i shifting elements to the left
# assuming i is a valid index
def removeMiddle(arr, i, length):
  # shift starting from i + 1 to end
  for index in range(i + 1, lenght):
    arr[index - 1] = arr[index]
  # no need to remove arr[i], since we already shifted

def printArr(arr, capacity):
  for i in range(capacity):
    print(arr[i])