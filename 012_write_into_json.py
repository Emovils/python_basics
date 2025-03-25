import json
student = {
        "id": 1,
        "name": "bola oluwole",
        "gender" : "male",
        "department": "computer science",
        "school": "OAU university"
}
with open("data_013_data.json", "w" ) as json_file:
    json.dump(student, json_file)
print("data successfully written into data_013_data.json")
