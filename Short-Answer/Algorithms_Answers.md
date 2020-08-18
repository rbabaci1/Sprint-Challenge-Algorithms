#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The runtime complexity of this piece of code is O(n^3)
The reason been is that the more input size n grows, the loop runs up n^3.

b) The runtime complexity of this piece of code is O(n^2)
The first loop runs over all the array in an O(n), the inner for loop
runs from 1 to the end of the array which is O(n) as well. Since one is inside the other
O(n) \* O(n) we get O(n^2)

c) The runtime complexity of this piece of code is O(n)
In a best case scenario bunnies will be equal to 0 so we don't get into the recursion
which would give us O(1), but in the worse case we would have a recursion that grows
proportionnelle with the size of bunnies which is the a linear time.

## Exercise II

- Lets say (n) is the number of floors in the building.
- and (f) would be the value of the highest floor we can drop eggs safely without breaking them.
- Our goal is to minimize the number of dropped eggs + broken eggs.
- Let's have a function called "drop_egg()" that takes an egg and through it from a certain floor
- A naive solution for this would be to start dropping from the first and if the egg doesn't break
  we can go one higher and do the same thing. When an egg breaks then we know that (f) is the floor before it.
- This algorithm runs in O(n) in the worst case where we have to go over all the floors.

- A better solution is using the concept of binary search.
- We first through the egg from (n/2), if the egg breaks, then we check the floors from 0 to n/2
- Otherwise, we through the egg from n/2 + (n - n/2) / 2 and we repeat the process.
- This algorithm would run in a O(log n) time.
