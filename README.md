
Hai Yuan hyuan12@stevens.edu

# bugs and issues

Case #5 in the timer class didn't pass, "t.stop()" raised an error after "t.reset()." I don't know why this is happening.

# resolved issue 

Then I looked carefully at the instruction and realized the problem was that the reset function should only reset the total but does not affect currently running timers.
