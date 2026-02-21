# ECM1414 - Data Structures and Algorithms CW - Group 35

## Description
This project analyses a list of activities that a University society could undertake over the course of a weekend. The aim is to maximise the enjoyment of the participants whilst keeping to a specified budget. This is achieved through two different algorithms: a brute force approach and a dynamically programmed approach. Both approaches are timed and their respective solutions are outputted in a human readable format. The project has been designed to interact with a specific format of input file, located in the `Input_Files` directory.

## How to run
 - Ensure you are in the directory that contains the `event_planner.py` script.
 - In the terminal, run the command: `python event_planner.py <file_name>`, where `<file_name>` is the name of the chosen sample file.
 - Example: `python event_planner.py input_small.txt`.

## File Structure
```
Group_35_ECM1414_Coursework.zip
├───Code/
│   │   brute_force.py
│   │   dynamic_method.py
│   │   event_planner.py
│   │   file_input.py
│   └───README.md
│
├───Documents/
│   │   Report.pdf
│   └───Group_Contribution_Statement.pdf
│       
├───Input_Files/
│   │   input_10.txt
│   │   input_100.txt
│   │   input_1000.txt
│   │   input_200.txt
│   │   input_500.txt
│   │   input_large.txt
│   │   input_medium.txt
│   └───input_small.txt
│       
└───Presentation/
    └───Presentation_Slides.pdf
```

## File Explanation
 - `Code/`
   - This directory contains all Python scripts used for our implementation of the Student Society Event Planner.
   - `brute_force.py` is the Python module that contains the brute force algorithmic approach.
   - `dynamic_method.py` is the more efficient approach to solving the problem.
   - `file_input.py` is the module that deals with parsing the input file.
 - `Documents/`
   - `Report.pdf` contains the in-depth explanation of the design and implementation of the algorithms, along with our testing and results.
   - `Group_Contribution_Statement.pdf` contains the contributions of each group member.
 - `Input_Files/`
   - This directory contains many sample input files.
   - File name structure: `input_x.txt`, where `x` represents the number of activities within the file.
 - `Presentation/`
   - `Presentation_Slides.pdf` is the 10-minute presentation talking about our implementation.

## Installation
Our modules were implemented using `Python 3.13`.

## Dependencies
Our implementation only requires built-in libraries. The libraries used are:
 - `sys` - used to extract terminal arguments and terminate the program.
 - `pathlib.Path` - used to construct the file path to the specified sample file, whilst being platform independent.
 - `time` - used to measure the execution time of each algorithm.
 - `itertools.combinations` - used to generate all subsets of a given size.

## Authors
 - Max Thrift-Brothers
 - Cameron Russell