student_1 = {"name": "susan",
             "Stream": "tech",
             "lessons done": "4",
             "completed_lessons":["variables","data_types", "dictionaries" ]}

print(student_1["Stream"])
student_1["completed_lessons"].remove("data_types")
print(student_1)