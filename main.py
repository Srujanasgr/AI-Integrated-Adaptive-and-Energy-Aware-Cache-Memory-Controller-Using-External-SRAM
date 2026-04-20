# main.py

from simulator.runner import run_all

# ===== INPUT =====
requests = list(map(int, input("Enter requests: ").split()))
cache_size = int(input("Enter cache size: "))

# ===== RUN =====
results = run_all(requests, cache_size)

# ===== OUTPUT =====
print("\n===== RESULTS =====")

for policy, rate in results.items():
    print(f"{policy} Hit Rate: {rate}")