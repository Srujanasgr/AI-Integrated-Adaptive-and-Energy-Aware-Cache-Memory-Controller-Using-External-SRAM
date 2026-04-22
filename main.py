from core.policies import lru, fifo, lfu

# Input
requests = list(map(int, input("Enter requests: ").split()))
cache_size = int(input("Enter cache size: "))

# Run
lru_hits, _ = lru(requests, cache_size)
fifo_hits, _ = fifo(requests, cache_size)
lfu_hits, _ = lfu(requests, cache_size)

total = len(requests)

# Output
print("\nResults:")
print("LRU Hit Rate:", lru_hits / total)
print("FIFO Hit Rate:", fifo_hits / total)
print("LFU Hit Rate:", lfu_hits / total)
