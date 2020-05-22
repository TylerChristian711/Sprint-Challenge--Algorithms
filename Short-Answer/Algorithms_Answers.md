#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N^2) because the loop is going over n^3 while the operation inside the loop is squaring n.
    which means it will only loop n^2 


b) O(n) , the second for loop is exponential growth which as the program scales it will have an ever increasing
    diminishing effect 


c) O(N) , since the recusion will pop only after it completed the 2 part dose not matter the recursion
            time per bunnyEars passed in which is O(N)

## Exercise II


if dropEggBreaks(0):
    return 0
if dropEggBreaks(1):
    return 1
while(maxLimit == float('inf')):
    if dropEggBreaks(currentFloor) == False:
            minLimit = currentFloor
            currentFloor *= currentFloor
    else
        maxLimit = currentFloor
 
while result == 0:
    if(maxLimit - minLimit == 1):
        result = maxLimit
    currentFloor = maxLimit - minLimit //2
    if dropEggBreaks(currentFloor) == false:
        minLimit = currentFloor
    else:
        maxLimit = currentFloor
        
return result
The Time complexity is O(1) since we're doing binary search the size of n doesn't significantly 
effect the number of operations as n scales.