#list into uppercase and stores them in a set
lst = ["Hello", "Hey", "Meet"]
s = {w.upper() for w in lst}
print(s)
'''
output:
{'HEY', 'MEET', 'HELLO'}
'''
#set containing 10 random numbers in the range 15 to 45.Delete,count.
import random
s = set(random.randint(15, 45) for _ in range(10))
print("Original set:", s)
print("Less than 30:", len([x for x in s if x < 30]))
s = {x for x in s if x <= 35}
print("After deletion:", s)
'''
output:
Original set: {34, 36, 38, 45, 18, 21, 22, 25, 30}
Less than 30: 4
After deletion: {34, 18, 21, 22, 25, 30}
'''
