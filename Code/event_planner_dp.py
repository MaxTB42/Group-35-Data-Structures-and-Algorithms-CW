import time
import dynamic_method as dm

start = time.time()
file = dm.file_to_list('../Input_Files/input_large.txt')
optimal_subsets = dm.dynamic_subsets(file)

print(f"Length of subset: {len(optimal_subsets)}")
print(f"Selected activities: {optimal_subsets}")
end = time.time()
print("Time taken:", end - start)
