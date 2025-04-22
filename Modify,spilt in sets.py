#add five new names to this set, modifies one existing name and deletes two names.
s = set()
s.update(["Aryan", "Meet", "Tom", "Jim", "Dwij"])
print("Initial:", s)
s.discard("Tom")
s.add("Hilag")
s.difference_update(["Meet", "Dwij"])
print("Final:", s)
'''
output
Initial: {'Jim', 'Dwij', 'Meet', 'Aryan', 'Tom'}
Final: {'Jim', 'Aryan', 'Hilag'}
'''
#spilt in set
names = {"Amit", "Amish", "Aryan", "Bobby", "Bala"}
a_set = {n for n in names if n.startswith("A")}
b_set = {n for n in names if n.startswith("B")}
print("A:", a_set)
print("B:", b_set)
'''
output:
A: {'Amit', 'Aryan', 'Amish'}
B: {'Bala', 'Bobby'}
'''
