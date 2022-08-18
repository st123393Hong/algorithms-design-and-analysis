# insertion sort(ascending)

arr=[23,12,45,8,9,31]
length = len(arr)

for j in range(1,length):

    key = arr[j]
    i=j-1
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        i=i-1
    arr[i+1] = key
    
print(f"after insertion sort(ascending),the array is {arr}")

# insertion sort(descending)

arr=[23,12,45,8,9,31]
length = len(arr)

for j in range(1,length):
    key = arr[j]
    i=j-1
    while i>=0 and arr[i]<key:
        arr[i+1]=arr[i]
        i=i-1
    arr[i+1] = key
    
print(f"after insertion sort(descending),the array is {arr}")

# merge sort(ascending)

def merge_sort(arr,p,r):
    
    if p<r:
        q = int((p+r)/2)
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        arr = merge(arr,p,q,r)
    return arr

def merge(arr,p,q,r):
    x = q-p+1
    y = r-q
    L = []
    R = []

    for i in range(x):
        L.append(arr[p+i-1])
   
    for j in range(y):
        R.append(arr[q+j])
    
    L.append(float('inf'))
    R.append(float('inf'))
    i=0
    j=0
    
        
    for k in range(p-1,r):    
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            j = j+1
            
    return arr

arr = [23,12,45,8,7,0,66,88]
p = 1
r=len(arr)
merge_sort(arr,p,r)
print(f"after merge sort(ascending),the array is {arr}")

# merge sort(descending)

def merge_sort(arr,p,r):
    
    if p<r:    
        q = int((p+r)/2)
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        arr = merge(arr,p,q,r)
    return arr
def merge(arr,p,q,r):
    x = q-p+1
    y = r-q
    L = []
    R = []

    for i in range(x):
        L.append(arr[p+i-1])
   
    for j in range(y):
        R.append(arr[q+j])
    
    L.append(float('-inf'))
    R.append(float('-inf'))
    i = 0
    j = 0

    for k in range(p-1,r):    
        if L[i] >= R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            j = j+1
            
    return arr

arr = [23,12,45,8,7,0,66,88]
p = 1
r = len(arr)
merge_sort(arr,p,r)
print(f"after merge sort(descending),the array is {arr}")