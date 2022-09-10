#quicksort
import timeit,random
def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<=x:
            i = i+1
            #exchange A[i] with A[j]
            num = A[j]
            A[j] = A[i]
            A[i] = num
    #exchange A[i+1] with A[r]
    num = A[r]
    A[r] = A[i+1]
    A[i+1] = num
    return i+1
def test():
    A = []
    for i in range(1000):
        A.append(random.randint(0,99))
    quicksort(A,0,len(A)-1)
    print(f"after quicksort,the array is:{A}")
ti = timeit.timeit(test,number=1)
print(ti)
