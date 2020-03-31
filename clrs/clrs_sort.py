import random

def selection_sort(A):
    N = len(A)
    for i in range(N):
        m = i
        for j in range(i+1, N):
            if A[j]<A[m]:
                m = j
        A[i], A[m] = A[m], A[i]

def insertion_sort(A):
    N = len(A)
    for j in range(1, N):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

def shell_sort(A):
    N = len(A)
    h = 1
    while h<N//3:
        h = 3*h+1
    while h>=1:
        for i in range(h, N):
            for j in range(i, h-1, -h):
                if A[j]>A[j-h]:
                    break
                A[j], A[j-h] = A[j-h], A[j]
        h = h//3

def bubble_sort(A):
    N = len(A)
    for i in range(0, N-1):
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j-1], A[j] = A[j], A[j-1]

def merge_sort(A):
    def merge(A, p, q, r):
        n1 = q-p+1
        n2 = r-q
        L = [A[p+i] for i in range(0, n1)]
        R = [A[q+i+1] for i in range(0, n2)]
        L.append(2**64)
        R.append(2**64)
        i = 0
        j = 0
        for k in range(p, r+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
    
    def sort(A, p, r):
        if p < r:
            q = (p+r)//2
            sort(A, p, q)
            sort(A, q+1, r)
            merge(A, p, q, r)
    
    N = len(A)
    sort(A, 0, N-1)

def quick_sort(A):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    def randomized_partition(A, p, r):
        i = random.randrange(0, r+1)
        A[r], A[i] = A[i], A[r]
        return partition(A, p, r)

    def sort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            sort(A, p, q-1)
            sort(A, q+1, r)
    
    N = len(A)
    sort(A, 0, N-1)

def heap_sort(A):
    def max_heapify(A, A_heapsize, i):
        l = left(i)
        r = right(i)
        if l <= A_heapsize and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r <= A_heapsize and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            max_heapify(A, A_heapsize, largest)
    
    def build_max_heap(A):
        N = len(A)
        A_heapsize = N
        A.insert(0, 0)
        for i in range(N//2+1, 0, -1):
            max_heapify(A, A_heapsize, i)
    
    def parent(i):
        return i//2

    def left(i):
        return 2*i
    
    def right(i):
        return 2*i+1

    N = len(A)
    A_heapsize = N
    build_max_heap(A)
    for i in range(len(A)-1, 1, -1):
        A[1], A[i] = A[i], A[1]
        A_heapsize = A_heapsize-1
        max_heapify(A, A_heapsize, 1)
    A.pop(0)