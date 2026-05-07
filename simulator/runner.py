# simulator/runner.py
#phase2
#phase 3 upadted code
from core.policies import lru, fifo, lfu, lru_optimized


# Strategy Pattern
POLICIES = {
    "LRU": lru,
    "FIFO": fifo,
    "LFU": lfu,
    "LRU_OPT": lru_optimized
}


def run_policy(policy_name, requests, cache_size):

    if policy_name not in POLICIES:
        raise ValueError("Invalid Policy")

    func = POLICIES[policy_name]

    hits, misses = func(requests, cache_size)

    total = len(requests)

    return {
        "hits": hits,
        "misses": misses,
        "hit_rate": hits / total,
        "miss_rate": misses / total
    }


def run_all(requests, cache_size):

    results = {}

    for name, func in POLICIES.items():

        hits, misses = func(requests, cache_size)

        results[name] = {
            "hit_rate": hits / len(requests),
            "miss_rate": misses / len(requests)
        }

    return results
