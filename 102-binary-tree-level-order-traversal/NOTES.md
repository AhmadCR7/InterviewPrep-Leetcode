Solution:
For this problem we use BFS approach meaning we use Queue data structure
We insert element to the right
Pop element from the left side
First in first out
The first level is [3] is in the queue we pop that element and added to sublist
When we pop the [3] we add the children to the queue [9][20]
We pop() and add them to it’s sublist
Since [9] did not had any children but [ 20] has 2 we put it to the queue
Now we hae [15][7] we pop() both and done
We return all of it as one sublist and return it as result
The time complexity is O(n) since we visit nodes once
The memory complexity O(n/2) = O(n)
​