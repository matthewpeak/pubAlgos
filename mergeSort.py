
def mergeSort(arr):
  if len(arr) == 1:
    return arr
  
  mid = round(len(arr)/2)
  
  left = mergeSort(arr[0:mid])
  right = mergeSort(arr[mid:])

  return merge(left,right)

def merge(left,right):
  i=0
  j=0
  merged=[]
  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      merged.append(left[i])
      i+=1
    else:
      merged.append(right[j])
      j+=1
  
  while i<len(left):
    merged.append(left[i])
    i+=1

  while j<len(right):
    merged.append(right[j])
    j+=1
  
  return merged


print(mergeSort([1,45,9,39,10,123,2,5,6,8,23]))
