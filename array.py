
# Array Implementation

arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

# Insert
arr.append(60)
print("After Insertion:", arr)

# Delete
arr.remove(30)
print("After Deletion:", arr)

# Search
if 40 in arr:
    print("40 found in the array")
else:
    print("Element not found")

# Update
arr[0] = 100
print("After Updating:", arr)

# Display
print("Final Array:", arr)
