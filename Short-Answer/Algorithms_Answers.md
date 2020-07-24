#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    The runtime of this code snippet would be Linear Time O(logn), 
    Our number of operation increases slightly as our number of input
    increases.

b)
    The runtime of this code snippet would be Quadratic or Polynomial O(n^c) due to the nested whild loop inside the for. Meaning the number of operations we preform greatly increases as our input size increases 

c)

    The runtime of this code snippet would be Logarithmic Time O(logn), 
    Our number of operation increases slightly as our number of input
    increases. This is because we are recursively calling our function again and again. Even if our input is large we'll slowly .........

## Exercise II


We want to determine floor f by breaking the least number of eggs 


1. Drop and egg from the current floor that we're on 
    if the egg breaks then we know that the current floor 
        we're on is floor f.

2. Else the egg remains unbroken
     therefore go move up one floor and repeat step 1 

the runtime of this solution would be linear time. The number of times we have to drop an egg to check what floor we're is continget on the number of floor we may have to traverse. 
