class MinHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self._bubble_up(len(self.heap) - 1)

    def build_heap(self, items):
        self.heap = [0] + items[:]
        for i in range(len(self.heap) // 2, 0, -1):
            self._bubble_down(i)

    def insert(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 1:
            return None
        min_item = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return min_item

    def _bubble_up(self, i):
        parent = i // 2
        if parent > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._bubble_up(parent)

    def _bubble_down(self, i):
        left_child = 2 * i
        right_child = 2 * i + 1
        smallest = i
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._bubble_down(smallest)


class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self._bubble_up(len(self.heap) - 1)

    def build_heap(self, items):
        self.heap = [0] + items[:]
        for i in range(len(self.heap) // 2, 0, -1):
            self._bubble_down(i)

    def insert(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 1:
            return None
        max_item = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return max_item

    def _bubble_up(self, i):
        parent = i // 2
        if parent > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._bubble_up(parent)

    def _bubble_down(self, i):
        left_child = 2 * i
        right_child = 2 * i + 1
        largest = i
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._bubble_down(largest)






# create a MinHeap object and insert some items
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(15)
min_heap.insert(20)
min_heap.insert(2)

# remove the min item from the heap
min_item = min_heap.remove()
print(f"Min item: {min_item}") # Output: Min item: 2

# create a MaxHeap object and insert some items
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(15)
max_heap.insert(20)
max_heap.insert(2)

# remove the max item from the heap
max_item = max_heap.remove()
print(f"Max item: {max_item}") # Output: Max item: 20




# Heap sort
# list of integers
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

arr = [34,56,23,45,94]
heap_sort(arr)
print(arr)


# list of strings

def heap_sort_str(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_str(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_str(arr, i, 0)

def heapify_str(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_str(arr, n, largest)

arr = ["Ramu","Raghav","Raghuvaran"]
heap_sort_str(arr)
print(arr)


# list of tuples with comparable data types
def heap_sort_tuple(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_tuple(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_tuple(arr, i, 0)

def heapify_tuple(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_tuple(arr, n, largest)

routes = [("Mumbai", "Delhi"),
          ("Mumbai", "Manali"),
          ("Kochi", "Pune"),
          ("Pune", "Mumbai"),
          ("Kochi", "Banglore"),
          ("Banglore", "Chennai"),
          ("Chennai", "Mumbai"),
          ("Chennai", "Hyderabad"),
          ("Hyderabad", "Pune"),
          ("Hyderabad", "Banglore")]

heap_sort_tuple(routes)
print(routes)