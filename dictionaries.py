def dictionary_operations():
    student = {
        "ID": 103,
        "Name": "Khushi",
        "Course": "Python",
        "Marks": 98
    }

    print("Student Dictionary")
    print("------------------")

    for key, value in student.items():
        print(f"{key}: {value}")

    student["Marks"] = 95
    student["City"] = "Delhi"

    print("\nUpdated Dictionary")
    print("------------------")

    for key, value in student.items():
        print(f"{key}: {value}")

    print("\nKeys:", student.keys())
    print("Values:", student.values())


if __name__ == "__main__":
    dictionary_operations()