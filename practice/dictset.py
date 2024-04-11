# wordmeaning = {"table": ["a piece of furniture",
#                          "list of facts & figures"], "cat": "a small animal"}
# print(wordmeaning)
# print(type(wordmeaning))

# set1 = {"python", "java", "c++", "python",
#         "javascript", "java", "python", "java", "c++", "c"}
# setlen = len(set1)
# print(f"The class room needed for set1 is {setlen}")
# print(type(set1))
marks = {}
x = int(input("Enter the phy:"))
marks.update({"Phy": x})
x = int(input("Enter the Mth: "))
marks.update({"Mth": x})
x = int(input("Enter the chem: "))
marks.update({"Chem": x})
print(marks)
