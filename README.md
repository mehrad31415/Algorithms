# Algorithms
This is a simple assignment comparing the performance of different algorithms. Specifically, the empirical results are tested against the theoretical formulas. 

# Sorting Algorithm Performance Analysis

This project investigates the performance of two sorting algorithms, Selection Sort and Merge Sort, through two separate experiments. The experiments focus on comparing the time complexity of these algorithms when sorting datasets.

## Algorithms and Code

- **Languages Used:** Java and Python
- The author has written the code for the basis of the comparison (Java) and for creating graphs (Python).
- The code for Selection Sort (Java) is entirely authored by the project creator.
- The code for Merge Sort has been sourced from the [geeksforgeeks website](https://www.geeksforgeeks.org/merge-sort/) [1].

## Experiment Methodology

The experiments involve executing each algorithm 5000 times, with the elapsed time recorded as follows:

1. Five hundred different arrays are created.
2. Both sorting algorithms are run ten times on each array.
3. For each execution, the time taken to sort the array is measured.
4. The average of the ten measurements is calculated, representing the ultimate recorded time for sorting using the specified algorithm.

## Experiments

### Experiment 1

- Focus: Comparing Selection Sort and Merge Sort using random permutations of data.
- Data: Randomly arranged arrays without any specific order, with no duplicate elements.

### Experiment 2

- Focus: Comparing Selection Sort and Merge Sort with data sorted in ascending order.
- Data: Sorted arrays with the possibility of duplicate values.

## Hypotheses

- Null Hypothesis: There is no significant difference in the execution times of the two sorting algorithms. Any observed variations are due to random chance.
- Alternative Hypothesis: There is a significant difference in the execution times between the two sorting algorithms.

## Results Presentation

- Results are presented through box plots and graphs.
- The acceptance or rejection of the null hypothesis is tested, and conclusions are provided.
- All execution times are measured in nanoseconds.
