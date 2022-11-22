# Python-Square-Root-Of-An-Integer

## Task Description
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

## Explanation
Middle is being calculated first, then, binary search is used to find the square root of a number. 
In binary search, the code compares the square of the mid value with the given square in each step, if square of the mid value matches the given square then, it returns the mid value (square root) else if the given square is not a perfect square then it will return the mid value of a perfect square which is close to the given square. Only floor values are considered. 

Contains while loop. 

Time Complexity: O(logn) where n is the given square root

Space Complexity: O(1) only variables are used to store data which are instant

