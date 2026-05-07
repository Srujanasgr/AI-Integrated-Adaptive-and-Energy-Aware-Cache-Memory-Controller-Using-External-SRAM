#phase1
#phase 2 updated
#pase 4 updated
# main.py
from simulator.runner import run_all
from simulator.workloads import random_workload
# GENERATE WORKLOAD
requests = random_workload(100)

#CACHE SIZE 
cache_size = 5
#RUN SIMULATION 
results = run_all(requests, cache_size)
#OUTPUT
print("\n===== RESULTS =====")

for policy, metrics in results.items():

    print(f"\n{policy}")

    print("Hit Rate:", metrics["hit_rate"])
    print("Miss Rate:", metrics["miss_rate"])
    print("Energy:", metrics["energy"])
    print("Latency:", metrics["latency"])
