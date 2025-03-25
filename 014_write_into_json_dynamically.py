import json
a = input("id")
b = input("first_name")
c = input("last_name")
d = input("email")
e = input("password")
user_dict = {"id": a,
             "first_name": b,
             "last_name": c,
             "email": d,
             "password": e
             }
with open("015_register.json", "w") as my_file:
          json.dump(user_dict, my_file)
