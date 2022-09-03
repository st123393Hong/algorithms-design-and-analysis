import random
from binarytree import build
def heapsort():
    A = []
    # to use index from 1,I set the first number of array is  0,but it is no use.
    A.append(0)
    for i in range(1,7):
        A.append(random.randint(0,99))
    print(f"the origin array is {A}")
   
    build_max_heap(A)
    #the first number is no use
    heap_size = len(A)-1
    for i in range(len(A)-1,1,-1):
        #exchange A[1] with A[i]
        x = A[i]
        A[i] = A[1]
        A[1] = x 
        heap_size = heap_size-1
        max_heapify(A,1,heap_size)
    print(f"after heapsort,the array is {A}")

def build_max_heap(A):
    heap_size = len(A)-1
    x = int((len(A)-1)/2)
    for i in range(x,0,-1):
        max_heapify(A,i,heap_size)   


def max_heapify(A,i,heap_size):
    #draw the tree after each exchange,not include the first number 0
    graphTree(A)
    #l = left(i)
    l = 2*i
    #r = right(i)
    r = 2*i+1
    
    if l<=heap_size and A[l]> A[i]:
        largest = l
    else:
        largest = i
    if r<=heap_size and A[r]>A[largest]:
        largest = r
    if largest !=i:
         #exchange A[i] with A[largest]
        x = A[largest]
        A[largest] = A[i]
        A[i] = x
         
        max_heapify(A,largest,heap_size)

#draw the tree after each exchange,not include the first number 0       
def graphTree(arr):
    new_arr = []
    for item in arr[1:]:
        new_arr.append(item)

    root = build(new_arr)
    print(root)

heapsort()
