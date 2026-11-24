import gc
import time

# Check automatic garbage collection
print("Garbage Collection Enabled:", gc.isenabled())

# Display initial garbage collection count
print("Initial GC Count:", gc.get_count())

# Create objects
class Demo:
    def __init__(self, name):
        self.name = name
        self.ref = None

# Create circular references
obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

obj1.ref = obj2
obj2.ref = obj1

# Delete references
del obj1
del obj2

print("Objects deleted")

# Measure manual garbage collection time
start = time.time()

collected = gc.collect()

end = time.time()

print("Garbage Collected:", collected)
print("Time Taken:", end - start)

# Display final garbage collection count
print("Final GC Count:", gc.get_count())

# Check memory management status
print("Garbage Collection Enabled:", gc.isenabled())
