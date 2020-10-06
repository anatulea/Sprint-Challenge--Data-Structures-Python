import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# --- METHOD 1 (0.2 sec)----
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True 
        if target < self.value: 
            if self.left == None:
                return False 
            return self.left.contains(target)
        else:
            if self.right == None:
                return False
            return self.right.contains(target)

binary_search_tree = BSTNode("")

duplicates = []  
for name in names_1:
    binary_search_tree.insert(name)
for name in names_2:
    if binary_search_tree.contains(name):
        duplicates.append(name)


# --- METHOD 2 (~ 1.3 sec)----
# duplicates = [elem for elem in names_2 if elem  in names_1 ]


# ---  GIVEN METHOD  (~ 9 sec)----
# duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
