import heapq
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

x = [1, 3 ,5, 7, 9, 2, 4, 6, 8, 10]
print(heapsort(x))
print(x)
heapq.heapify(x)
print(x)
print([heapq.heappop(x) for i in range(len(x))])
