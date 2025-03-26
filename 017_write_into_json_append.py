import json
with open("016_data.json", "r") as file:
    my_list_dict =json.load(file)
data_dict ={
        "id": input("enter your id: "),
        "first_name": input("enter your first name"),
        "last_name": input("enter yoour last name"),
        "email": input ("email address"),
        "password": input("password")
         }
my_list_dict.append(data_dict)
with open("016_data.json", "w") as file:
     json.dump(my_list_dict, file)
print("user data successfully appended to 016_data.json")
