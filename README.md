
Hai Yuan hyuan12@stevens.edu

# bugs and issues

when trying to test the longest_lines function, it was saying, "No such file or 
directory." I don't know why this is happening.

# resolved issue 

when dealing with DPS and BFS the first time, there are some nodes that 
haven't been visited. Then I realized that the problem is that these nodes don't 
have any connection with the previous. So I need to start a loop searching with 
the smallest node that hasn't yet visited.