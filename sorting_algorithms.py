# File: sorting_algorithms.py

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def analyze_bubble_sort(n):
    return f"""
    Bubble Sort Time Complexity:
    - Worst-case: O(n^2) - {n**2} comparisons
    - Best-case: O(n) - {n} comparisons (when the array is already sorted)
    - Average-case: O(n^2) - {n**2 // 2} comparisons

    Space Complexity: O(1) - In-place sorting algorithm

    Bubble Sort repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. 
    The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
    """

def analyze_insertion_sort(n):
    return f"""
    Insertion Sort Time Complexity:
    - Worst-case: O(n^2) - {n**2 // 2} comparisons and swaps
    - Best-case: O(n) - {n - 1} comparisons (when the array is already sorted)
    - Average-case: O(n^2) - {n**2 // 4} comparisons and swaps

    Space Complexity: O(1) - In-place sorting algorithm

    Insertion Sort builds the final sorted array one item at a time. It iterates through an input array and 
    removes one element per iteration, finds the location it belongs within the sorted list and inserts it there. 
    It repeats until no input elements remain.
    """

def analyze_quicksort(n):
    return f"""
    Quicksort Time Complexity:
    - Worst-case: O(n^2) - {n**2 // 2} comparisons (rare, happens when the pivot is always the smallest or largest element)
    - Best-case: O(n log n) - {n * (n.bit_length())} comparisons
    - Average-case: O(n log n) - {n * (n.bit_length())} comparisons

    Space Complexity: O(log n) - Due to the recursive call stack

    Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and 
    partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. 
    The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.
    """