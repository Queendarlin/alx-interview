# N Queens Problem

The N Queens problem is a classic puzzle in which you must place N queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

## Description

This project provides a Python solution to the N Queens problem using a backtracking algorithm. The program finds all possible ways to place N non-attacking queens on an N×N chessboard.

## Usage

To run the program, use the following command:

```sh
python 0-nqueens.py N
```
Where N is the size of the chessboard (and also the number of queens to place). The program will print all possible solutions, one solution per line.
* The program must be called with exactly one argument: the integer N.
* N must be an integer greater than or equal to 4.
* If these conditions are not met, the program will print an appropriate error message and exit with status 1.

## Algorithm
The solution uses a backtracking algorithm:

* Check Safety: A helper function is_safe checks if it's safe to place a queen at a given position.
* Backtracking: The main recursive function attempts to place queens row by row, backtracking when a conflict is detected.
* Solution Storage: Valid solutions are stored and printed.

## Files
0-nqueens.py: The main script containing the solution to the N Queens problem.

## Requirements
Python 3.x

## Installation
* Clone the repository:
```sh
git clone https://github.com/Queendarlin/alx-interview.git
```
* Navigate to the project directory:

```sh
cd alx-interview/0x05-nqueens
```

## Running the Script
To run the script with a specific value of N, use the command line:
```sh
python 0-nqueens.py 4
```

## Author
This project was developed by [Queendarlin Nnamani](https://github.com/Queendarlin?tab=repositories)
