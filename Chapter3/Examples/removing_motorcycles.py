motorcycles = ['honda', 'suzuki', 'ducati', 'yamaha']

del motorcycles[0]
print(motorcycles)
print("\n")

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print("\n")

motorcycles = ['honda', 'suzuki', 'ducati', 'yamaha']

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print("\n")

motorcycles = ['honda', 'suzuki', 'ducati', 'yamaha']

popped_motorcycles = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycles)
print("\n")

motorcycles = ['honda', 'suzuki', 'ducati', 'yamaha']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")