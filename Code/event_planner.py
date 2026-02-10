"""
This is the main entry point for the coursework.
It uses the two algorihtms to produce the optimal subset of activities.
It then produces a human readable output of the optimal solution.
"""

# Used for the command line argument "input_file_name"
import sys
# Used to access the input files in the Input_Files directory
from pathlib import Path

# Output the title
print("========================================")
print("Event Planner - Results")
print("========================================")

# Extract the file name
input_file_name = sys.argv[1]
