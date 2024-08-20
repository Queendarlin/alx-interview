# Coin Change Problem

## Overview

The Coin Change Problem is a classic algorithmic problem in the domain of dynamic programming and greedy algorithms. The goal is to determine the minimum number of coins needed to make a given total amount using a list of available coin denominations.

This project involves implementing a solution to this problem in Python, ensuring that the algorithm is both correct and efficient.

## Problem Description

Given a list of coin denominations and a total amount, the task is to find the minimum number of coins needed to make up the total amount. If it is not possible to make the total amount using the given coins, the function should return `-1`.

### Function Prototype

```python
def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of integers representing the denominations of the coins.
        total (int): The target amount to be reached using the coins.
    
    Returns:
        int: The fewest number of coins needed to reach the total amount, or -1 if it is not possible.
    """

### Installation

Clone this repository:
git clone https://github.com/Queendarlin/alx-interview.git
cd alx-interview/0x08-making_change
