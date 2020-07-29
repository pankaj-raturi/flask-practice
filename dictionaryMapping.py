#!/usr/bin/env python3

users = [
    (1, "Rob", "123"),
    (2, "Bob", "345"),
    (3, "Sara", "678")
]

users_mapping = {user[1]: user for user in users}
users_mapping_new = {user[1]: {"id":user[0], "password": user[2]} for user in users}

print(users)
print(users_mapping)
print(users_mapping_new)