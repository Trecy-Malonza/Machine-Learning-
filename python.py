import heapq

heap = [20,40,30,40]
heapq.heapify(heap)
heapq.heappush(heap,50)
heapq.heappop(heap)
largestElement = heapq.nlargest(1,heap)[0]
print(heap)
print(largestElement)

heap3 = ["Mary","Caren","Zippy"]
heapq.heapify(heap3)
heapq.heappop(heap3)
print(heap3)
heapq.heappush(heap3,"Tracy")
print(heap3)


def max_heapify(A, k):
    l = left(k)
    r = right(k) 
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)
def left(k):
    return 2 * k + 1
def right(i): 
    return 2 * i + 2 
def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A, k)
A = [3, 9, 2, 1, 4, 5]
build_max_heap(A)
print(A)
