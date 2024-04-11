info = {
    "name": "Pawan Acharya",
    "age": 25,
    "subjects_mark": {
        "phy": 99,
        "chem": 98,
        "math": 100
    },
    "cast": "Bharmin",
    "available": True
}
# print(info)
# print(info["subjects_mark"])
# print(info.get("cast"))
# print(len(list(info.keys())))
# print(len(info))
# print(list(info.values()))
# print(info["cast"])
# print(info.get("cast1"))
info.update({"rollno": 34})
print(info)
