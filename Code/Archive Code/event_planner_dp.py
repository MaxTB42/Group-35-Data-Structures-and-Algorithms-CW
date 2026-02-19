import time
import dynamic_method as dm
import file_input_new as fi


start = time.time()
optimal_subsets = dm.dynamic_subsets(fi.file_input('../Input_Files/input_1000.txt'))

print(f"Length of subset: {len(optimal_subsets[0])}")
print(f"Selected activities: {optimal_subsets}")
end = time.time()
print("Time taken:", end - start)
