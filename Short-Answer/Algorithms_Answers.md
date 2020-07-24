#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    The runtime of this code is linear time O(n). No matter the size of our input 
    our runtime porpotional to our input size. 

b)
    The runtime is O(log(n)). Despite there being a nested while loop the amount of operations we must doe inside the for loop is the same which is O(n) and doesn't care what the actual unput size is. the while loop is making the comparison and incrementing. 

c)
    This will return an infinte loop because we never reach our base case. O(n)
    because you only can input 0. 






## Exercise II


We want to determine floor f by breaking the least number of eggs 

1. start at the very first floor

2. Drop and egg from the current floor that we're on 
    if the egg breaks then we know that the current floor 
        we're on is floor f.

3. Else the egg remains unbroken
     therefore go move up one floor and repeat step 2

the runtime of this solution would be linear time. The number of times we have to drop an egg to check what floor we're is continget on the number of floor we may have to traverse. 
