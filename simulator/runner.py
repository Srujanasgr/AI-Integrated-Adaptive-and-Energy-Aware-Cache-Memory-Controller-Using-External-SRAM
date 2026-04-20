# simulator/runner.py

from core.policies import lru, fifo, lfu, lru_optimized


POLICIES = {
    "LRU": lru,
    "FIFO": fifo,
    "LFU": lfu,
    "LRU_OPT": lru_optimized
}


def run_policy(policy_name, requests, cache_size):
    if policy_name not in POLICIES:
        raise ValueError("Invalid policy")

    func = POLICIES[policy_name]
    hits, misses = func(requests, cache_size)

    total = len(requests)
    hit_rate = hits / total
    miss_rate = misses / total

    return {
        "hits": hits,
        "misses": misses,
        "hit_rate": hit_rate,
        "miss_rate": miss_rate
    }


def run_all(requests, cache_size):
    results = {}

    for name, func in POLICIES.items():
        hits, misses = func(requests, cache_size)
        total = len(requests)

        results[name] = hits / total

    return results