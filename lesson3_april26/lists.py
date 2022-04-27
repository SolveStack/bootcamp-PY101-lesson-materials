numbered_list = ['zero', 'one', 'two', 'three']
print("Accessing an item in the list:")
print(numbered_list[0])
print("getting the index of each of the list items:")
for item, index in enumerate(numbered_list):
    print(f"item: {item}")
    print(f"index: {index}")



print(f"Length of numbered list: {len(numbered_list)}")
numbered_list.append('four')
print(f"New length of numbered list: {len(numbered_list)}")

# Remove a four
numbered_list.remove('four')
print(numbered_list)


print(f"Index of 'one': {numbered_list.index('one')}")
print("Removing 'zero'")
numbered_list.remove('zero')
print(numbered_list)


print("Removing 'zero'")
try:
    numbered_list.remove('zero')
except ValueError:
    print("No zero, moving on.")
    pass

print("Starting value:")
print(numbered_list)
print(f"length of list: {len(numbered_list)}")
numbered_list.append("three")
print("Three added to the list again:")
print(f"length of list: {len(numbered_list)}")
print("Ending value:")
print(numbered_list)


