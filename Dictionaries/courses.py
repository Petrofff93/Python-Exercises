def print_func(courses_dict):
    for (course, people) in courses_dict.items():
        print(f"{course}: {len(people)}")
        for person in people:
            print(f"-- {person}")


def courses():
    courses_dict = dict()

    while True:
        command = input()
        if command == "end":
            print_func(courses_dict)
            break

        command = command.split(" : ")
        course_name = command[0]
        person_name = command[1]
        my_list = [person_name]
        if course_name not in courses_dict:
            courses_dict[course_name] = my_list
        else:
            courses_dict[command[0]] += my_list


courses()
