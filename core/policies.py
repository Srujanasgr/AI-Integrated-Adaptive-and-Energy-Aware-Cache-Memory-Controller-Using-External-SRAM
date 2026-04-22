def lru(requests, cache_size):
    cache = []
    hits, misses = 0, 0

    for req in requests:
        if req in cache:
            hits += 1
            cache.remove(req)
            cache.append(req)
        else:
            misses += 1
            if len(cache) == cache_size:
                cache.pop(0)
            cache.append(req)

    return hits, misses


def fifo(requests, cache_size):
    cache = []
    hits, misses = 0, 0

    for req in requests:
        if req in cache:
            hits += 1
        else:
            misses += 1
            if len(cache) == cache_size:
                cache.pop(0)
            cache.append(req)

    return hits, misses


def lfu(requests, cache_size):
    cache = []
    freq = {}
    hits, misses = 0, 0

    for req in requests:
        if req in cache:
            hits += 1
            freq[req] += 1
        else:
            misses += 1
            if len(cache) == cache_size:
                lfu_item = min(cache, key=lambda x: freq[x])
                cache.remove(lfu_item)
                del freq[lfu_item]

            cache.append(req)
            freq[req] = 1

    return hits, misses
