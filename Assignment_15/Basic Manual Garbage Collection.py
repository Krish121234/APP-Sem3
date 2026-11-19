import gc

# Returns the number of objects it has collected and deallocated
collected = gc.collect()

print("Garbage collector: collected", "%d objects." % collected)