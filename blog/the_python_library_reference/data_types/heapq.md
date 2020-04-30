This module provides an implementation of the heap queue algorithm, also known as **the priority queue algorithm**.

Heaps are binary trees for which every parent node has a value less than or equal to any of its children. This implementation uses **arrays** for which `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all k, counting elements from zero. For the sake of comparison, non-existing elements are considered to be infinite. The interesting property of a heap is that its smallest element is always the root, `heap[0]`.

To create a heap, use a list initialized to `[]`, or you can transform a populated list into a heap via function `heapify()`.

The following functions are provided:

- `heapq.heappush(heap, item)`
- `heapq.heappop(heap)`
- `heapq.heappushpop(heap, item)`
- `heapq.heapreplace(heap, item)`
- `heapq.heapify(x)`

The module also offers three general purpose functions based on heaps.

- `heapq.merge(*iterables, key=None, reverse=False)`
- `heapq.nlargest(n, iterable, key=None)`
- `heapq.nsmallest(n, iterable, key=None)`

> The latter two functions perform best for smaller values of n. For larger values, it is more efficient to use the `sorted()` function. Also, when `n==1`, it is more efficient to use the built-in `min()` and `max()` functions. If repeated usage of these functions is required, consider turning the iterable into an actual heap.
