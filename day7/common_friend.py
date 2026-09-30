manisha_friends = {"Rahul", "Priya", "Aman", "Neha"}
rahul_friends = {"Priya", "Aman", "Ravi", "Karan"}

print("Mutual friends:")
print(manisha_friends.intersection(rahul_friends))

print("Combined friends:")
print(manisha_friends.union(rahul_friends))

print("Only Manisha's friends:")
print(manisha_friends.difference(rahul_friends))

print("Exclusive friends:")
print(manisha_friends.symmetric_difference(rahul_friends))