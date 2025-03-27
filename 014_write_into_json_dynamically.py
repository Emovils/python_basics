import json
a = input("enter your id:")
b = input("enter your first_name")
c = input("enter your last_name")
d = input("enter your email")
e = input("password")
user_dict = {"id": a,
             "first_name": b,
             "last_name": c,
             "email": d,
             "password": e
             }
with open("015_register.json", "w") as my_file:
          json.dump(user_dict, my_file)
