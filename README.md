
Hai Yuan hyuan12@stevens.edu

# bugs and issues

One issue I encountered while writing and testing my code was related to the computation of the swap count in a sorting algorithm. I had instrumented the algorithm to count the number of swaps by incrementing a counter variable every time a swap was performed. When I ran the algorithm on a large input, I noticed that the swap count was much higher than expected.


# resolved issue 

After some investigation, I realized that the swap count was being incremented twice for each swap operation, because the algorithm was swapping two elements in the array twice in some cases.

To fix the issue, I modified the swap function to check whether the two elements being swapped were already in the correct order before performing the swap. If they were, I skipped the swap operation and did not increment the swap count. This eliminated the double counting of swaps and produced accurate statistics for the algorithm.