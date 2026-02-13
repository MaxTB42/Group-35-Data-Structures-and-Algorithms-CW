import time
import dynamic_method as dm
import dynamic_method_extension as dms


start = time.time()
file = dm.file_to_list('../Input_Files/input_large.txt')
optimal_subsets = dm.dynamic_subsets(file)

print(f"Length of subset: {len(optimal_subsets)}")
print(f"Selected activities: {optimal_subsets}")
end = time.time()
print("Time taken:", end - start)

start = time.time()
file = dms.file_to_list('../Input_Files/input_large.txt')
optimal_subsets = dms.dynamic_subsets(file)

print(f"Length of subset: {len(optimal_subsets)}")
print(f"Selected activities: {optimal_subsets}")
end = time.time()
print("Time taken:", end - start)
