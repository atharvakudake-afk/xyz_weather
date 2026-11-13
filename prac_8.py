#heapify: fix the heap of the subtree whose root is index 1.
# n is the size of the heap part of the array.
def heapify(arr, n, i):
    largest = i   # assume the root is largest
    left = 2*i+1  #index of left child
    right = 2*i+2  #index of right child

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i] , arr[largest] = arr[largest] ,arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    #step 1: built a max heap (starting from the last parent and go up)
    for i in range(n // 2 - 1, -1 , -1):
        heapify(arr, n, i)
    print("Max heap built   :", arr)

    for i in range(n - 1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i , 0)
        print("After moving ", arr[i], "to end:", arr)

numbers = [12, 11, 13, 5, 6, 7]
print("Original arra: ", numbers)

heap_sort(numbers)

print("Sorted array       :", numbers)
