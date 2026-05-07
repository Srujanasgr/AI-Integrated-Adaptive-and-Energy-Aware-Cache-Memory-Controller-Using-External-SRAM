#phase1
#phase 2 updated
#phase 4 updated
#phase 5 upadted
# main.py
# MAIN PROJECT FILE 

from simulator.runner import run_all
from simulator.workloads import random_workload
from ml.features import extract_features
#  GENERATE WORKLOAD 
requests = random_workload(100)

#  CACHE SIZE 
cache_size = 5
# FEATURE EXTRACTION 
features = extract_features(requests)

# RUN SIMULATION 
results = run_all(requests, cache_size)

#  PRINT REQUESTS 
print("\n===== WORKLOAD =====")
print(requests)

# PRINT FEATURES 
print("\n===== FEATURES =====")

for key, value in features.items():
    print(f"{key}: {value}")

# PRINT RESULTS 
print("\n===== RESULTS =====")

for policy, metrics in results.items():

    print(f"\n{policy}")

    print("Hit Rate:", metrics["hit_rate"])
    print("Miss Rate:", metrics["miss_rate"])
    print("Energy:", metrics["energy"])
    print("Latency:", metrics["latency"])
    
