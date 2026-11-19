import gc

i = 0

# Create a cycle on each iteration where x is a dictionary referencing itself
def create_cycle():
    x = {}
    x[i + 1] = x
    print(x)

collected = gc.collect()  # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))

print("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()
print("Garbage collector: collected %d objects." % (collected))